import pygame
import math

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Extended Paint in Pygame")

# Дополнительный слой, на котором будем хранить нарисованное
base_layer = pygame.Surface((WIDTH, HEIGHT))
base_layer.fill((255, 255, 255))  # зальём белым фоном

clock = pygame.time.Clock()

# Цвета
colorRED = (255, 0, 0)
colorGREEN = (0, 255, 0)
colorBLUE = (0, 0, 255)
colorBLACK = (0, 0, 0)
colorWHITE = (255, 255, 255)

current_color = colorRED  # Текущий цвет рисования

# Инструменты (modes):
#  - 'line'  (простой карандаш, как в оригинале)
#  - 'rect'  (прямоугольник)
#  - 'circle'(круг)
#  - 'eraser'(ластик)
mode = 'line'

drawing = False   # Флаг зажатия ЛКМ
start_pos = (0, 0)# Точка, где нажали ЛКМ (для rect/circle)
thickness = 5

def draw_line(surface, color, start, end, thickness):
    """ Рисуем линию (карандашом). """
    pygame.draw.line(surface, color, start, end, thickness)

def draw_rect(surface, color, start, end, thickness):
    """ Рисуем прямоугольник от start до end. """
    rect = pygame.Rect(min(start[0], end[0]),
                       min(start[1], end[1]),
                       abs(start[0] - end[0]),
                       abs(start[1] - end[1]))
    pygame.draw.rect(surface, color, rect, thickness)

def draw_circle(surface, color, start, end, thickness):
    """
    Рисуем окружность, ограниченную прямоугольником
    от start до end. Радиус = расстояние между start и end / 2.
    Центр = средняя точка между start и end.
    """
    center_x = (start[0] + end[0]) // 2
    center_y = (start[1] + end[1]) // 2
    radius = int(math.sqrt((end[0] - start[0])**2 + (end[1] - start[1])**2) / 2)
    # Если thickness == 0, получится залитый круг. 
    # Чтобы сделать контур, передаём thickness в аргумент width=
    pygame.draw.circle(surface, color, (center_x, center_y), radius, thickness)

def erase(surface, pos, size):
    """ Ластик: рисуем белым квадратом (или кругом) в месте pos. """
    eraser_rect = pygame.Rect(pos[0] - size//2, pos[1] - size//2, size, size)
    pygame.draw.rect(surface, colorWHITE, eraser_rect)

running = True
while running:
    screen.fill(colorWHITE)            # Очищаем основной экран
    screen.blit(base_layer, (0, 0))    # Отрисовываем слой со «статическим» рисунком поверх

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

            # Цвет
            if event.key == pygame.K_r:
                current_color = colorRED
            elif event.key == pygame.K_g:
                current_color = colorGREEN
            elif event.key == pygame.K_b:
                current_color = colorBLUE
            elif event.key == pygame.K_k:  # k -> black
                current_color = colorBLACK

            # Толщина
            if event.key == pygame.K_EQUALS:
                thickness += 1
            elif event.key == pygame.K_MINUS:
                thickness = max(1, thickness - 1)

        # Обрабатываем нажатие ЛКМ
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # ЛКМ
                drawing = True
                start_pos = event.pos

        # Обрабатываем отпускание ЛКМ
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:  # ЛКМ
                drawing = False
                end_pos = event.pos

                # По окончании рисования (rect/circle/line)
                if mode == 'rect':
                    draw_rect(base_layer, current_color, start_pos, end_pos, thickness)
                elif mode == 'circle':
                    draw_circle(base_layer, current_color, start_pos, end_pos, thickness)
                # Если mode == 'line', то мы уже нарисовали линии по ходу движения
                # Если mode == 'eraser', то тоже уже стерли по ходу
                # => Только rect/circle нужно «финализировать»

        # Движение мыши в зажатом состоянии
        if event.type == pygame.MOUSEMOTION and drawing:
            current_pos = event.pos

            if mode == 'line':
                # Рисуем сразу на base_layer, чтобы линии не исчезали
                draw_line(base_layer, current_color, start_pos, current_pos, thickness)
                start_pos = current_pos  # двигаем "начальную" точку дальше
            elif mode == 'eraser':
                # Стираем небольшим квадратом
                erase(base_layer, current_pos, thickness * 2)

    # Если пользователь «тянет» прямоугольник или круг, покажем «предпросмотр»:
    # (рисуем поверх screen, но не сохраняем в base_layer, пока не отпустят мышь)
    if drawing and (mode == 'rect' or mode == 'circle'):
        mouse_pos = pygame.mouse.get_pos()
        if mode == 'rect':
            draw_rect(screen, current_color, start_pos, mouse_pos, thickness)
        elif mode == 'circle':
            draw_circle(screen, current_color, start_pos, mouse_pos, thickness)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()