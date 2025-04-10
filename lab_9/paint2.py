import pygame
import math

pygame.init()

WIDTH = 800
HEIGHT = 600

# Создаём окно
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Дополнительный слой, на котором будем хранить нарисованное
base_layer = pygame.Surface((WIDTH, HEIGHT))
base_layer.fill((255, 255, 255))  # заливаем фон

# запускаем время (фпс=60)
clock = pygame.time.Clock()

# определяем вета
colorRED = (255, 0, 0)
colorGREEN = (0, 255, 0)
colorBLUE = (0, 0, 255)
colorBLACK = (0, 0, 0)
colorWHITE = (255, 255, 255)

current_color = colorRED  # Текущий цвет рисования

'''
Инструменты (modes):
'line'  (простой карандаш, как в оригинале)
'rect'  (прямоугольник)
'circle'(круг)
'eraser'(ластик)
'square' - квадрат
'rtriangle' - прямоугольный треугольник
'triangle'  - равносторонний треугольник
'rhombus'   - ромб
'''
mode = 'line'


drawing = False   # проверка зажатия ЛКМ
start_pos = (0, 0)# место где нажали ЛКМ (для rect/circle)
thickness = 5

# Функции рисования (все принимают surface, color, start, end, thickness)
def draw_line(surface, color, start, end, thickness):
    # Рисуем линию (карандашом) 
    pygame.draw.line(surface, color, start, end, thickness)

def draw_rect(surface, color, start, end, thickness):
    # Рисуем прямоугольник от start до end 
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
    # Если thickness == 0, получится залитый круг
    # Чтобы сделать контур, передаём thickness в аргумент width
    pygame.draw.circle(surface, color, (center_x, center_y), radius, thickness)

def erase(surface, pos, size):
    # Ластик: рисуем белым квадратом (или кругом) в месте pos
    eraser_rect = pygame.Rect(pos[0] - size//2, pos[1] - size//2, size, size)
    pygame.draw.rect(surface, colorWHITE, eraser_rect)

def draw_square(surface, color, start, end, thickness):
    """
    Рисуем квадрат. Сторона = max по ширине/высоте
    bounding-box от start до end.
    """
    left = min(start[0], end[0])
    top = min(start[1], end[1])
    side = max(abs(end[0] - start[0]), abs(end[1] - start[1]))
    rect = pygame.Rect(left, top, side, side)
    pygame.draw.rect(surface, color, rect, thickness)

def draw_rtriangle(surface, color, start, end, thickness):
    """
    Рисуем прямоугольный треугольник.
    Чтобы «замкнуть» фигуру, используем 3 точки:
     A = start
     B = (start.x, end.y)
     C = end
    """
    (x1, y1) = start
    (x2, y2) = end
    # Точки (A, B, C) – 3 вершины треугольника
    A = (x1, y1)
    B = (x1, y2)
    C = (x2, y2)
    pygame.draw.polygon(surface, color, [A, B, C], thickness)

def draw_equilateral_triangle(surface, color, start, end, thickness):
    """
    Рисуем равносторонний треугольник, у которого отрезок (start -> end)
    является одной из сторон. Третья вершина вычисляется исходя
    из высоты h = (sqrt(3)/2)*side.
    """
    x1, y1 = start
    x2, y2 = end
    
    # Длина стороны:
    side = math.dist(start, end)
    
    # Центр отрезка (start -> end)
    cx = (x1 + x2) / 2
    cy = (y1 + y2) / 2
    
    # Угол наклона отрезка (start->end)
    angle = math.atan2((y2 - y1), (x2 - x1))
    
    # Высота равностороннего треугольника
    height = side * (math.sqrt(3) / 2)
    
    # Координаты третьей вершины (x3, y3)
    # Двигаемся от середины перпендикулярно отрезку на расстояние height
    x3 = cx + height * math.cos(angle + math.pi / 2)
    y3 = cy + height * math.sin(angle + math.pi / 2)

    pygame.draw.polygon(surface, color, [(x1, y1), (x2, y2), (x3, y3)], thickness)

def draw_rhombus(surface, color, start, end, thickness):
    # Рисуем ромб, вписанный в bounding-box между start и end.
    left = min(start[0], end[0])
    right = max(start[0], end[0])
    top = min(start[1], end[1])
    bottom = max(start[1], end[1])

    cx = (left + right) / 2
    cy = (top + bottom) / 2

    # Четыре вершины ромба
    top_point = (cx, top)
    right_point = (right, cy)
    bottom_point = (cx, bottom)
    left_point = (left, cy)

    points = [top_point, right_point, bottom_point, left_point]
    pygame.draw.polygon(surface, color, points, thickness)

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
            elif event.key == pygame.K_5:
                mode = 'square'
            elif event.key == pygame.K_6:
                mode = 'rtriangle'
            elif event.key == pygame.K_7:
                mode = 'triangle'
            elif event.key == pygame.K_8:
                mode = 'rhombus'

            # Цвет (клавиши r/g/b/k соответствуют красному/зеленому/синему/черному)
            if event.key == pygame.K_r:
                current_color = colorRED
            elif event.key == pygame.K_g:
                current_color = colorGREEN
            elif event.key == pygame.K_b:
                current_color = colorBLUE
            elif event.key == pygame.K_k: 
                current_color = colorBLACK

            # Толщина (клавиши + и -)
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
                ''' 
                Если mode == 'line', то мы уже нарисовали линию по ходу движения
                Если mode == 'eraser', то тоже уже стерли по ходу
                Остальное нужно отрисовывать после предпросмотра
                '''

                if mode == 'rect':
                    draw_rect(base_layer, current_color, start_pos, end_pos, thickness)
                elif mode == 'circle':
                    draw_circle(base_layer, current_color, start_pos, end_pos, thickness)
                elif mode == 'square':
                    draw_square(base_layer, current_color, start_pos, end_pos, thickness)
                elif mode == 'rtriangle':
                    draw_rtriangle(base_layer, current_color, start_pos, end_pos, thickness)
                elif mode == 'triangle':
                    draw_equilateral_triangle(base_layer, current_color, start_pos, end_pos, thickness)
                elif mode == 'rhombus':
                    draw_rhombus(base_layer, current_color, start_pos, end_pos, thickness)


        #Движение мыши в зажатом состоянии
        if event.type == pygame.MOUSEMOTION and drawing:
            current_pos = event.pos

            if mode == 'line':
                # Рисуем сразу на base_layer, чтобы линии не исчезали 
                draw_line(base_layer, current_color, start_pos, current_pos, thickness)
                start_pos = current_pos
            elif mode == 'eraser':
                # Стираем небольшим квадратом
                erase(base_layer, current_pos, thickness * 2)

    # «Предпросмотр» фигур не сохраняя их на base_layer
    if drawing and mode in ('rect', 'circle', 'square', 'rtriangle', 'triangle', 'rhombus'):
        mouse_pos = pygame.mouse.get_pos()
        if mode == 'rect':
            draw_rect(screen, current_color, start_pos, mouse_pos, thickness)
        elif mode == 'circle':
            draw_circle(screen, current_color, start_pos, mouse_pos, thickness)
        elif mode == 'square':
            draw_square(screen, current_color, start_pos, mouse_pos, thickness)
        elif mode == 'rtriangle':
            draw_rtriangle(screen, current_color, start_pos, mouse_pos, thickness)
        elif mode == 'triangle':
            draw_equilateral_triangle(screen, current_color, start_pos, mouse_pos, thickness)
        elif mode == 'rhombus':
            draw_rhombus(screen, current_color, start_pos, mouse_pos, thickness)



    pygame.display.flip()
    clock.tick(60)

pygame.quit()