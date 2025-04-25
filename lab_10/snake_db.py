"""
При первом запуске user‑имя добавляется в snake_user.
Каждый раз при паузе/выходе текущий score записывается в user_score.
SELECT * FROM snake_user;  -- Должна вернуть список пользователей
SELECT * FROM user_score;  -- Должна вернуть сохранённые счёты
"""

# ──────────────────────────────────────────────────────────────────────
# импорт
# ──────────────────────────────────────────────────────────────────────
import math, random, sys
import pygame
from color_palette import *
try:
    import psycopg2
    from config import load_config          # функция чтения database.ini
    DB_ENABLED = True
except (ImportError, FileNotFoundError):
    DB_ENABLED = False                      # можно играть без БД

# ──────────────────────────────────────────────────────────────────────
# настройки окна
# ──────────────────────────────────────────────────────────────────────
pygame.init()
WIDTH, HEIGHT = 600, 600
CELL         = 30          # размер клетки
COLS, ROWS   = WIDTH//CELL, HEIGHT//CELL
screen       = pygame.display.set_mode((WIDTH, HEIGHT))
clock        = pygame.time.Clock()

# ──────────────────────────────────────────────────────────────────────
# вспомогательные классы
# ──────────────────────────────────────────────────────────────────────
class Point:
    def __init__(self, x:int, y:int):  self.x, self.y = x, y
    def __iter__(self): return iter((self.x, self.y))
    def __eq__(self, other): return self.x==other.x and self.y==other.y

class Snake:
    def __init__(self):
        self.body = [Point(10,11), Point(10,12), Point(10,13)]
        self.dx, self.dy = 1, 0
    def move(self):
        # сдвигаем тело
        for i in range(len(self.body)-1, 0, -1):
            self.body[i].x, self.body[i].y = self.body[i-1].x, self.body[i-1].y
        # перемещаем голову
        self.body[0].x += self.dx
        self.body[0].y += self.dy
        # сквозные стены
        self.body[0].x %= COLS
        self.body[0].y %= ROWS
    def grow(self):
        tail = self.body[-1]
        self.body.append(Point(tail.x, tail.y))
    def head(self): return self.body[0]
    # проверка столкновения со стеной или своим телом
    def hits_itself(self):
        return any(seg == self.head() for seg in self.body[1:])
    def hits_point(self, pt): return self.head() == pt
    def draw(self):
        pygame.draw.rect(screen, colorRED,
                         (self.head().x*CELL, self.head().y*CELL, CELL, CELL))
        for seg in self.body[1:]:
            pygame.draw.rect(screen, colorYELLOW,
                             (seg.x*CELL, seg.y*CELL, CELL, CELL))

class Food:
    def __init__(self): self.pos = Point(5,5)
    def place(self, snake, walls):
        while True:
            x, y = random.randrange(COLS), random.randrange(ROWS)
            p = Point(x,y)
            if p not in snake.body and p not in walls: break
        self.pos = p
    def draw(self):
        pygame.draw.rect(screen, colorGREEN,
                         (self.pos.x*CELL, self.pos.y*CELL, CELL, CELL))

class Wall(list):
    def __init__(self): super().__init__()
    def generate(self, level, snake):
        """для каждого уровня рисуем новые стены"""
        self.clear()
        if level == 1: return                  # первый уровень без стен
        if level == 2:
            # горизонтальная линия посередине, но оставляем дырку 6 клеток
            for x in range(COLS):
                if abs(x - snake.head().x) < 3: continue
                self.append(Point(x, ROWS//2))
        elif level == 3:
            # прямоугольник‑рамка
            for x in range(COLS):
                self += [Point(x,0), Point(x,ROWS-1)]
            for y in range(ROWS):
                self += [Point(0,y), Point(COLS-1,y)]
        else:
            # случайные блоки, гарантируя дистанцию от головы >4
            for _ in range(15 + 5*(level-4)):
                while True:
                    p = Point(random.randrange(COLS), random.randrange(ROWS))
                    if (abs(p.x - snake.head().x) > 4 or
                        abs(p.y - snake.head().y) > 4):
                        if p not in self: break
                self.append(p)
    def draw(self):
        for pt in self:
            pygame.draw.rect(screen, colorPURPLE,
                             (pt.x*CELL, pt.y*CELL, CELL, CELL))
            
def draw_grid_chess():
    colors = [colorWHITE, colorGRAY]          # клетка‑светлая / клетка‑тёмная
    for i in range(ROWS):
        for j in range(COLS):
            pygame.draw.rect(
                screen,
                colors[(i + j) % 2],          # чётные ↔ нечётные
                (j * CELL, i * CELL, CELL, CELL)
            )


# ──────────────────────────────────────────────────────────────────────
# функции базы данных (опционально)
# ──────────────────────────────────────────────────────────────────────
def db_get_or_create_user(username:str):
    if not DB_ENABLED: return None
    cfg = load_config()
    with psycopg2.connect(**cfg) as conn:
        with conn.cursor() as cur:
            cur.execute("INSERT INTO snake_user(username) "
                        "VALUES(%s) ON CONFLICT (username) DO NOTHING "
                        "RETURNING user_id;", (username,))
            row = cur.fetchone()
            if row: return row[0]                  # новый пользователь
            # иначе получить id существующего
            cur.execute("SELECT user_id FROM snake_user WHERE username=%s;",
                        (username,))
            return cur.fetchone()[0]

def db_get_latest_score(user_id:int):
    if not DB_ENABLED: return None,None
    cfg = load_config()
    with psycopg2.connect(**cfg) as conn, conn.cursor() as cur:
        cur.execute("""SELECT score, level
                       FROM   user_score
                       WHERE  user_id=%s
                       ORDER  BY score_id DESC
                       LIMIT 1;""", (user_id,))
        row = cur.fetchone()
        return row if row else (0,1)

def db_insert_score(user_id:int, score:int, level:int):
    if not DB_ENABLED: return
    cfg = load_config()
    with psycopg2.connect(**cfg) as conn, conn.cursor() as cur:
        cur.execute("""INSERT INTO user_score(user_id, score, level)
                       VALUES (%s,%s,%s);""", (user_id, score, level))

# ──────────────────────────────────────────────────────────────────────
# меню имени пользователя
# ──────────────────────────────────────────────────────────────────────
def ask_username():
    pygame.display.set_caption("Enter username…")
    font = pygame.font.SysFont("Verdana", 32)
    buffer = ""
    while True:
        screen.fill(colorBLACK)
        txt = font.render("Enter username:", True, colorWHITE)
        screen.blit(txt, (60, 150))
        usertxt = font.render(buffer + "|", True, colorGREEN)
        screen.blit(usertxt, (60, 220))
        pygame.display.flip()

        for e in pygame.event.get():
            if e.type == pygame.QUIT: sys.exit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_RETURN and buffer:
                    return buffer
                elif e.key == pygame.K_BACKSPACE:
                    buffer = buffer[:-1]
                elif e.unicode.isprintable() and len(buffer) < 20:
                    buffer += e.unicode

# ──────────────────────────────────────────────────────────────────────
# основная игра
# ──────────────────────────────────────────────────────────────────────
def main():
    username = ask_username()
    user_id  = db_get_or_create_user(username)
    saved_score, saved_level = db_get_latest_score(user_id) if user_id else (0,1)

    snake = Snake()
    food  = Food()
    walls = Wall()
    level = saved_level
    score = saved_score
    FPS   = 5 + 2*(level-1)

    walls.generate(level, snake)
    food.place(snake, walls)

    paused = False
    fontUI = pygame.font.SysFont("Verdana", 20)

    while True:
        # ─ события
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                if user_id: db_insert_score(user_id, score, level)
                sys.exit()
            if e.type == pygame.KEYDOWN:
                if e.key in (pygame.K_RIGHT, pygame.K_d): snake.dx, snake.dy = 1,0
                if e.key in (pygame.K_LEFT,  pygame.K_a): snake.dx, snake.dy =-1,0
                if e.key in (pygame.K_DOWN,  pygame.K_s): snake.dx, snake.dy = 0,1
                if e.key in (pygame.K_UP,    pygame.K_w): snake.dx, snake.dy = 0,-1
                if e.key == pygame.K_p:      # pause / unpause
                    paused = not paused
                    if paused and user_id:
                        db_insert_score(user_id, score, level)

        if paused:
            pygame.display.set_caption("Snake – paused (P to resume)")
            clock.tick(10)
            continue
        else:
            pygame.display.set_caption("Snake")

        # ─ логика
        snake.move()
        if snake.hits_itself() or snake.head() in walls:
            if user_id: db_insert_score(user_id, score, level)
            return                      # game over → выйдем в ask_username

        # еда
        if snake.hits_point(food.pos):
            score += 1; snake.grow()
            food.place(snake, walls)
            if score >= level*3:        # каждые 3 очка → новый уровень
                level += 1
                FPS += 2
                walls.generate(level, snake)
                # убедиться, что еда не в стене
                food.place(snake, walls)

        # ─ отрисовка
        draw_grid_chess()
        for pt in walls:                 # рисуем стены
            pygame.draw.rect(screen, colorBLUE,
                             (pt.x*CELL, pt.y*CELL, CELL, CELL))
        snake.draw()
        food.draw()
        ui = fontUI.render(
            f"{username}  Score:{score}  Level:{level}", True, colorBLACK)
        screen.blit(ui, (10, 10))
        pygame.display.flip()
        clock.tick(FPS)

# ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    while True:
        main()      # после game‑over возвращаемся к экрану имени