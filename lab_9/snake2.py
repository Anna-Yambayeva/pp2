import pygame
from color_palette import * # Импортируем цвета из color_palette.py
import random # Импортируем random для генерации случайных чисел

pygame.init()

WIDTH = 600
HEIGHT = 600

# Устанавливаем размеры окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Устанавливаем размер клеток
CELL = 30

# определяем функции для рисования сетки (на выбор - обычная или шахматная)
def draw_grid(): # обычная сетка
    for i in range(HEIGHT // CELL):
        for j in range(WIDTH // CELL):
            pygame.draw.rect(screen, colorGRAY, (i * CELL, j * CELL, CELL, CELL), 1)

def draw_grid_chess(): # шахматная сетка
    colors = [colorWHITE, colorGRAY]

    for i in range(HEIGHT // CELL):
        for j in range(WIDTH // CELL):
            pygame.draw.rect(screen, colors[(i + j) % 2], (i * CELL, j * CELL, CELL, CELL))

class Point:    # класс для хранения координат
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x}, {self.y}"

class Snake:   # класс змейки
    def __init__(self): # задаем начальные координаты
        self.body = [Point(10, 11), Point(10, 12), Point(10, 13)]
        self.dx = 1
        self.dy = 0

    def move(self): # для движения змейки
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y

        self.body[0].x += self.dx
        self.body[0].y += self.dy

        # проверяем столкновение с границами и отключаем игру при проигрыше
        if self.body[0].x >= WIDTH // CELL or self.body[0].x < 0 or self.body[0].y >= HEIGHT // CELL or self.body[0].y < 0:
            pygame.quit()
            exit()


    def draw(self): # для рисования змейки
        head = self.body[0]
        pygame.draw.rect(screen, colorRED, (head.x * CELL, head.y * CELL, CELL, CELL))
        for segment in self.body[1:]:
            pygame.draw.rect(screen, colorYELLOW, (segment.x * CELL, segment.y * CELL, CELL, CELL))

    def check_collision(self, food): # проверяем столкновение с едой
        head = self.body[0]
        if head.x == food.pos.x and head.y == food.pos.y: # если голова змейки совпадает с позицией еды то увеличиваем длину змейки
            print("Got food!")
            self.body.append(Point(head.x, head.y))
            if isinstance(food, SuperFood): 
                food.generate_random_pos(self, food) # Генерируем новую позицию для супер еды
            else:
                food.generate_random_pos(self) # Генерируем новую позицию для обычной еды
            return True  # Вернём True, чтобы увеличить счёт
        return False

class Food: # класс еды
    def __init__(self):
        self.pos = Point(9, 9)

    def draw(self): # для рисования еды
        pygame.draw.rect(screen, colorGREEN, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL)) # рисуем еду

    def generate_random_pos(self, snake): # генерируем случайную позицию для еды которая не совпадает с телом змейки
        while True:
            x = random.randint(0, WIDTH // CELL - 1)
            y = random.randint(0, HEIGHT // CELL - 1)
            
            overlap = False
            for segment in snake.body: 
                if segment.x == x and segment.y == y:
                    overlap = True
                    break
            
            if not overlap:
                self.pos = Point(x, y)
                break

class SuperFood: # класс супер еды
    def __init__(self):
        self.pos = Point(1, 3)
        self.timer = 0
        self.max_time = 60  # Время жизни супер еды (в кадрах)

    def draw(self):
        #  Определяем цвет в зависимости от времени жизни
        remaining_time = self.max_time - self.timer
        if remaining_time > self.max_time // 2:
            color = colorPURPLE
        else:
            color = colorPINK

        pygame.draw.rect(screen, color, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL)) # рисуем супер еду

    def generate_random_pos(self, snake, food): # генерируем случайную позицию для супер еды которая не совпадает с телом змейки и не совпадает с позицией обычной еды
        while True:
            x = random.randint(0, WIDTH // CELL - 1)
            y = random.randint(0, HEIGHT // CELL - 1)
            
            # Проверим, что (x, y) не занято телом змейки и не совпадает с позицией обычной еды
            overlap = False
            for segment in snake.body:
                if segment.x == x and segment.y == y:
                    overlap = True
                    break
            if x == food.pos.x and y == food.pos.y:
                overlap = True
            
            if not overlap:
                self.pos = Point(x, y)
                self.timer = 0  # Сбросим таймер при генерации новой супер еды
                break

# Запускаем время (фпс=5)
FPS = 5
clock = pygame.time.Clock()

# создаем объекты еды и змейки
food = Food()
super_food = SuperFood()
snake = Snake()

score = 0          # Счёт
level = 1          # Уровень
score_for_next_level = 3  # каждые 3 очка -> следующий уровень

# шрифт, чтобы выводить счёт и уровень
font = pygame.font.SysFont("Verdana", 20)

running = True
while running:
    for event in pygame.event.get(): # обрабатываем события
        if event.type == pygame.QUIT: # если нажали на крестик
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT: # если нажали на стрелку вправо
                snake.dx = 1
                snake.dy = 0
            elif event.key == pygame.K_LEFT: # если нажали на стрелку влево
                snake.dx = -1
                snake.dy = 0
            elif event.key == pygame.K_DOWN: # если нажали на стрелку вниз
                snake.dx = 0
                snake.dy = 1
            elif event.key == pygame.K_UP: # если нажали на стрелку вверх
                snake.dx = 0
                snake.dy = -1

    screen.fill(colorBLACK)

    draw_grid_chess()  # рисуем шахматную сетку (опционально заменить на простую..)

    snake.move()
    if snake.check_collision(food):
        # Если еда съедена, повышаем счёт, генерируем еду в новом месте
        score += 1
        food.generate_random_pos(snake)

        # Проверяем, не пора ли перейти на новый уровень (каждые 3 очка)
    if score >= level * score_for_next_level:
        level += 1
        # Увеличим скорость
        FPS += 2

    #  Проверяем столкновение с супер едой
    if snake.check_collision(super_food):
        score += 5  #  Увеличиваем счёт на 5 за супер еду
        super_food.generate_random_pos(snake, food)

    #  Обновляем таймер супер еды
    super_food.timer += 1
    if super_food.timer >= super_food.max_time:
        super_food.generate_random_pos(snake, food)
    super_food.draw()

    # Рисуем змейку и еду
    snake.draw()
    food.draw()

    # Рисуем счёт и уровень
    score_text = font.render(f"Score: {score}   Level: {level}", True, colorBLACK)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()