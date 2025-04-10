import pygame
import math

pygame.init()

#создаем окно
WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Extended Paint in Pygame")

# Дополнительный слой для хранения рисунка
base_layer = pygame.Surface((WIDTH, HEIGHT))
base_layer.fill((255, 255, 255))  # фон
clock = pygame.time.Clock()

# Определяем цвета
colorRED = (255, 0, 0)
colorGREEN = (0, 255, 0)
colorBLUE = (0, 0, 255)
colorBLACK = (0, 0, 0)
colorWHITE = (255, 255, 255)

current_color = colorRED  # Текущий цвет

# Инструменты
modes = ['line', 'rect', 'circle', 'eraser', 'right_triangle', 'equilateral_triangle', 'rhombus']
mode = 'line'  # Инструмент по умолчанию

drawing = False
start_pos = (0, 0)
thickness = 5

#расписываем функции для рисования заданных фигур

def draw_line(surface, color, start, end, thickness):
    pygame.draw.line(surface, color, start, end, thickness)

def draw_rect(surface, color, start, end, thickness):
    rect = pygame.Rect(min(start[0], end[0]),
                       min(start[1], end[1]),
                       abs(start[0] - end[0]),
                       abs(start[1] - end[1]))
    pygame.draw.rect(surface, color, rect, thickness)

def draw_circle(surface, color, start, end, thickness):
    center_x = (start[0] + end[0]) // 2
    center_y = (start[1] + end[1]) // 2
    radius = int(math.sqrt((end[0] - start[0])**2 + (end[1] - start[1])**2) / 2)
    pygame.draw.circle(surface, color, (center_x, center_y), radius, thickness)

def draw_right_triangle(surface, color, start, end, thickness):
    points = [start, (start[0], end[1]), end]
    pygame.draw.polygon(surface, color, points, thickness)

def draw_equilateral_triangle(surface, color, start, end, thickness):
    base_x = start[0]
    base_y = start[1]
    height = abs(end[1] - base_y)
    points = [
        (base_x, base_y),
        (base_x - height, base_y + height),
        (base_x + height, base_y + height)
    ]
    pygame.draw.polygon(surface, color, points, thickness)

def draw_rhombus(surface, color, start, end, thickness):
    center_x = (start[0] + end[0]) // 2
    center_y = (start[1] + end[1]) // 2
    dx = abs(end[0] - start[0]) // 2
    dy = abs(end[1] - start[1]) // 2
    points = [(center_x, start[1]), (end[0], center_y), (center_x, end[1]), (start[0], center_y)]
    pygame.draw.polygon(surface, color, points, thickness)

def erase(surface, pos, size):
    eraser_rect = pygame.Rect(pos[0] - size//2, pos[1] - size//2, size, size)
    pygame.draw.rect(surface, colorWHITE, eraser_rect)

running = True
while running:
    screen.fill(colorWHITE)               # Очищаем основной экран
    screen.blit(base_layer, (0, 0))       # Отрисовываем слой со «статическим» рисунком поверх

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Нажатия клавиш для изменения инструмента / цвета / толщины
        if event.type == pygame.KEYDOWN:
            # Инструменты
            if event.key == pygame.K_1:
                mode = 'line'
            elif event.key == pygame.K_2:
                mode = 'rect'
            elif event.key == pygame.K_3:
                mode = 'circle'
            elif event.key == pygame.K_4:
                mode = 'eraser'
            elif event.key == pygame.K_5:
                mode = 'right_triangle'
            elif event.key == pygame.K_6:
                mode = 'equilateral_triangle'
            elif event.key == pygame.K_7:
                mode = 'rhombus'
            # Цвет
            if event.key == pygame.K_r:
                current_color = colorRED
            elif event.key == pygame.K_g:
                current_color = colorGREEN
            elif event.key == pygame.K_b:
                current_color = colorBLUE
            elif event.key == pygame.K_k:
                current_color = colorBLACK
            # Толщина
            if event.key == pygame.K_EQUALS:
                thickness += 1
            elif event.key == pygame.K_MINUS:
                thickness = max(1, thickness - 1)

        # Зажали ЛКМ
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                drawing = True
                start_pos = event.pos
        
        # Отпустили ЛКМ
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                drawing = False
                end_pos = event.pos

                '''
                Если завершаем рисование:
                mode == 'line' - мы уже нарисовали линии по ходу движения
                mode == 'eraser' - тоже уже стерли по ходу
                Остальное нужно закрепить на основном слое
                '''
                if mode == 'rect':
                    draw_rect(base_layer, current_color, start_pos, end_pos, thickness)
                elif mode == 'circle':
                    draw_circle(base_layer, current_color, start_pos, end_pos, thickness)
                elif mode == 'right_triangle':
                    draw_right_triangle(base_layer, current_color, start_pos, end_pos, thickness)
                elif mode == 'equilateral_triangle':
                    draw_equilateral_triangle(base_layer, current_color, start_pos, end_pos, thickness)
                elif mode == 'rhombus':
                    draw_rhombus(base_layer, current_color, start_pos, end_pos, thickness)

        # При движении с зажатой ЛКМ БЕЗ фигуры
        if event.type == pygame.MOUSEMOTION and drawing:
            current_pos = event.pos
            if mode == 'line':
                draw_line(base_layer, current_color, start_pos, current_pos, thickness)
                start_pos = current_pos
            elif mode == 'eraser':
                erase(base_layer, current_pos, thickness * 2)

    # Если движение с зажатой ЛКМ С фигурой --> делаем предпросмотр (рисуем поверх screen, но не сохраняем в base_layer, пока не отпущена ЛКМ)
    if drawing and mode in ['rect', 'circle', 'right_triangle', 'equilateral_triangle', 'rhombus']:
        mouse_pos = pygame.mouse.get_pos()
        if mode == 'rect':
            draw_rect(screen, current_color, start_pos, mouse_pos, thickness)
        elif mode == 'circle':
            draw_circle(screen, current_color, start_pos, mouse_pos, thickness)
        elif mode == 'right_triangle':
            draw_right_triangle(screen, current_color, start_pos, mouse_pos, thickness)
        elif mode == 'equilateral_triangle':
            draw_equilateral_triangle(screen, current_color, start_pos, mouse_pos, thickness)
        elif mode == 'rhombus':
            draw_rhombus(screen, current_color, start_pos, mouse_pos, thickness)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
