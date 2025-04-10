import pygame
from datetime import datetime # импортируем datetime для получения текущего времени

pygame.init()

# создаем окно
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# загружаем изображения часов и стрелок
image = pygame.image.load('clock.png')
im_MIN = pygame.image.load('min_hand.png')
im_SEC = pygame.image.load('sec_hand.png')

# устанавливаем размеры изображений стрелок
rect_MIN = im_MIN.get_rect(center=(WIDTH // 2, HEIGHT // 2))
rect_SEC = im_SEC.get_rect(center=(WIDTH // 2, HEIGHT // 2))

# запускаем время (фпс=60)
clock = pygame.time.Clock()


running = True
while running:
    # если нажата кнопка выхода, то выходим из цикла
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# очищаем экран
    screen.blit(image, (0, 0))
# перемещаем стрелки в центр окна и устанавливаем их по текущему времени
    x = datetime.now()
    minuti = x.minute
    angleM = minuti * (-6) - 55

# устанавливаем угол поворота стрелки минут
    im_MIN_r = pygame.transform.rotate(im_MIN, angleM)
    rect_MIN_r = im_MIN_r.get_rect(center=rect_MIN.center)
# устанавливаем угол поворота стрелки секунд
    secu = x.second
    angleS = secu * (-6) + 60
    im_SEC_r = pygame.transform.rotate(im_SEC, angleS)
    rect_SEC_r = im_SEC_r.get_rect(center=rect_SEC.center)

# отображаем стрелки на экране
    screen.blit(im_MIN_r, rect_MIN_r.topleft)
    screen.blit(im_SEC_r, rect_SEC_r.topleft)

# обновляем экран чтобы все было видно
    pygame.display.flip()
    clock.tick(60)