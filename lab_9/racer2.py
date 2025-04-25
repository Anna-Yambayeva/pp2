import pygame, sys # sys для выхода из программы
from pygame.locals import * # импортируем константы из pygame.locals такие как QUIT, K_UP и т.д.
import random, time # random для генерации случайных чисел, time для задержки
 
#запускаемся
pygame.init()
 
#Запускаем время (фпс=60)
FPS = 60
FramePerSec = pygame.time.Clock()
 
#Библиотека цветов
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
 
# Другие переменные для дальнейшей работы
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
COIN_SCORE = 0
health=3
 
# Шрифт 
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)
 
# Загружаем фоновое изображение
background = pygame.image.load("imgs/AnimatedStreet.png")
 
# Создаем окно
DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
# отображаем game в заголовке окна
pygame.display.set_caption("Game")
 
class Enemy(pygame.sprite.Sprite): # наследуем класс от pygame.sprite.Sprite для создания врага
      def __init__(self): 
        super().__init__()  
        self.image = pygame.image.load("imgs/Enemy.png") # загружаем изображение врага
        self.rect = self.image.get_rect()   # получаем прямоугольник изображения
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)  # рандомно задаем координаты по оси Х
 
      def move(self): # метод движения врага
        global SCORE 
        self.rect.move_ip(0,SPEED) # двигаем врага вниз по оси Y
        if (self.rect.top > 600): # если враг выходит за пределы экрана
            SCORE += 1 
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0) # задаем новые координаты по оси Y

class Coin(pygame.sprite.Sprite): # наследуем класс от pygame.sprite.Sprite для создания монеты
      def __init__(self): 
        super().__init__() 
        self.image = pygame.transform.scale_by(pygame.image.load("imgs/coin.png").convert_alpha(), 0.035) # загружаем изображение монеты и уменьшаем его в 3 раза
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)  # рандомно задаем координаты по оси Х
 
      def move(self): # метод движения монеты
        self.rect.move_ip(0, SPEED) # двигаем монету вниз по оси Y
        if (self.rect.top > 600): # если монета выходит за пределы экрана
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0) # задаем новые координаты по оси Y
 
class Coin2(pygame.sprite.Sprite): # (идентично первой)
      def __init__(self): 
        super().__init__() 
        self.image = pygame.transform.scale_by(pygame.image.load("imgs/coin2.png").convert_alpha(), 0.07)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)  
 
      def move(self):
        self.rect.move_ip(0, SPEED)
        if (self.rect.top > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
 
class Player(pygame.sprite.Sprite): # наследуем класс от pygame.sprite.Sprite для создания игрока
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("imgs/Player.png") # загружаем изображение игрока
        self.rect = self.image.get_rect() # получаем прямоугольник изображения
        self.rect.center = (160, 520)   # задаем координаты игрока по оси Х и Y
        
    def move(self): # метод движения игрока
        pressed_keys = pygame.key.get_pressed() # привязываем движение к клавишам
        if pressed_keys[K_UP]: 
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0,5)
         
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:  # Если игрок пробует выйти за пределы экрана    
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)
                   
# Создаем игрока, врага и монеты       
P1 = Player()
E1 = Enemy()
С1 = Coin()
С2 = Coin2()

# Создаем группы для контроля столкновения
enemies = pygame.sprite.Group()
enemies.add(E1) 
coins = pygame.sprite.Group()
coins.add(С1)
coins2 = pygame.sprite.Group()
coins2.add(С2)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(С1)
all_sprites.add(С2)

 

while True:
    
    # Обрабатываем события
    for event in pygame.event.get():    
        if event.type == QUIT: # если нажали на крестик
            pygame.quit()
            sys.exit()
 
    DISPLAYSURF.blit(background, (0,0)) # заливаем фон c окном
    scores = font_small.render(str(SCORE), True, BLACK) # отображаем счёт
    coin_scores1 = font_small.render("Coins: ", True, BLACK) # отображаем текст "Coins: "
    coin_scores2 = font_small.render(str(COIN_SCORE), True, BLACK) # отображаем счёт монет
    DISPLAYSURF.blit(scores, (10,10)) 
    DISPLAYSURF.blit(coin_scores1, (SCREEN_WIDTH - 75, 10)) 
    DISPLAYSURF.blit(coin_scores2, (SCREEN_WIDTH - 50, 30))
 
    # Отрисовываем игрока, врага и монеты
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()
    
    # Проверяем столкновение игрока с врагом
    if pygame.sprite.spritecollideany(P1, enemies):
          pygame.mixer.Sound('imgs/crash.wav').play()
          health-=1
          E1.rect.top = 0
          E1.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
          if health==0:
            time.sleep(0.5) # задержка на 0.5 секунды
                    
            DISPLAYSURF.fill(RED) # заливаем экран красным цветом
            DISPLAYSURF.blit(game_over, (30,250)) # отображаем текст "Game Over"
           
            pygame.display.update() # обновляем экран
            for entity in all_sprites: 
                  entity.kill() 
            time.sleep(2)
            pygame.quit()
            sys.exit() 
          

    # Проверяем столкновение игрока с монетами
    coins_collided = pygame.sprite.spritecollide(P1, coins, True)
    for coin in coins_collided: # если столкновение произошло
        COIN_SCORE += 1
        coin.rect.top = 0 
        coin.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0) # задаем новые координаты по оси Y
        coins.add(coin)
        all_sprites.add(coin) 

    # идетично для второй монеты
    coins2_collided = pygame.sprite.spritecollide(P1, coins2, True)
    for coin2 in coins2_collided:
        COIN_SCORE += 2
        coin2.rect.top = 0
        coin2.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
        coins2.add(coin2)
        all_sprites.add(coin2)  

    # Увеличиваем скорость врага и монет в зависимости от счёта
    SPEED += (COIN_SCORE//5)/200        
        
    pygame.display.update()
    FramePerSec.tick(FPS)