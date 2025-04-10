import pygame
import random
import time

pygame.init() # инициализация библиотеки pygame

WIDTH = 400
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT)) # устанавливаем размеры окна которое принимает tuple как аргумент

background = pygame.image.load('imgs/AnimatedStreet.png') # загружаем фоновое изображение

running = True

# Запускаем время (фпс=60)
clock = pygame.time.Clock()
FPS = 60 

player_img = pygame.image.load('imgs/Player.png') # загружаем изображение игрока
enemy_img = pygame.image.load('imgs/Enemy.png') # загружаем изображение врага

# загружаем звуковые файлы
background_music = pygame.mixer.music.load('imgs/background.wav')
crash_sound = pygame.mixer.Sound('imgs/crash.wav')

# загружаем шрифты и надписи
font = pygame.font.SysFont("Verdana", 60)
game_over = font.render("Game Over", True, "black")

pygame.mixer.music.play(-1) # включаем фоновую музыку в бесконечном цикле

PLAYER_SPEED = 5 # скорость игрока
ENEMY_SPEED = 10 # скорость врага

class Player(pygame.sprite.Sprite): # класс игрока
    def __init__(self):
        super().__init__()
        self.image = player_img # загружаем изображение игрока
        self.rect = self.image.get_rect() # получаем прямоугольник игрока
        self.rect.x = WIDTH // 2 - self.rect.w // 2 
        self.rect.y = HEIGHT - self.rect.h 
    
    def move(self): # метод движения игрока
        keys = pygame.key.get_pressed() 
        # если нажата клавиша, то двигаем игрока в соответствующем направлении
        if keys[pygame.K_LEFT]:
            self.rect.move_ip(-PLAYER_SPEED, 0) 
        if keys[pygame.K_RIGHT]:
            self.rect.move_ip(PLAYER_SPEED, 0) 
        # если игрок выходит за границы окна, то возвращаем его обратно
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

class Enemy(pygame.sprite.Sprite): # класс врага
    def __init__(self):
        super().__init__()
        self.image = enemy_img
        self.rect = self.image.get_rect()
        self.generate_random_rect() # генерируем случайное положение врага на экране
    
    def move(self): # метод движения врага
        self.rect.move_ip(0, ENEMY_SPEED) # двигаем врага вниз
        if self.rect.top > HEIGHT:
            self.generate_random_rect()
    
    def generate_random_rect(self): # метод генерации случайного положения врага на экране
        self.rect.x = random.randint(0, WIDTH - self.rect.w)
        self.rect.y = 0


player = Player() # player's sprite
enemy = Enemy() # enemy's sprite

all_sprites = pygame.sprite.Group() # создаем общую группу
enemy_sprites = pygame.sprite.Group() # создаем группу врагов

all_sprites.add([player, enemy]) # добавляем игрока и врага в общую группу
enemy_sprites.add([enemy]) # добавляем врага в группу врагов

while running:
    for event in pygame.event.get(): # обрабатываем события
        if event.type == pygame.QUIT: # если нажата кнопка закрытия окна, то выходим из игры
            running = False
    
    screen.blit(background, (0, 0))

    player.move()
    enemy.move()

    for entity in all_sprites: 
        screen.blit(entity.image, entity.rect) # отрисовываем все спрайты на экране

    if pygame.sprite.spritecollideany(player, enemy_sprites): # если игрок столкнулся с врагом, то
        crash_sound.play()
        time.sleep(1)

        screen.fill("red")
        center_rect = game_over.get_rect(center = (WIDTH // 2, HEIGHT // 2))
        screen.blit(game_over, center_rect)

        pygame.display.flip()

        time.sleep(2)
        running = False


    
    pygame.display.flip() 
    clock.tick(FPS) 

pygame.quit()