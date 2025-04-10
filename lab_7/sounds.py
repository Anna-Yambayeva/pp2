import pygame
import os # для работы с путями файлов

pygame.init()

# создаем окно
screen = pygame.display.set_mode((800, 600))

running = True

# запускаем время (фпс=60)
clock = pygame.time.Clock()

# получаем доступ к файлами
songs = [
    "Mark Ronson,Bruno Mars - Uptown Funk.mp3",
    "ACDC - Highway to Hell.mp3",
    "The Neighbourhood - Sweater Weather.mp3"
]

current_song_index = 0

# создаем функцию для запуска музыки
def play_song(index):
    pygame.mixer.music.load(songs[index])
    pygame.mixer.music.play()

# создаем функцию для остановки музыки
def stop_music():
    pygame.mixer.music.stop()

# создаем функцию для переключения на следующую песню
def next_song():
    global current_song_index
    current_song_index = (current_song_index + 1) % len(songs)
    play_song(current_song_index)

# создаем функцию для переключения на предыдущую песню
def previous_song():
    global current_song_index
    current_song_index = (current_song_index - 1) % len(songs)
    play_song(current_song_index)


while running:
    # устанавливаем кнопки для управления
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                play_song(current_song_index)
            if event.key == pygame.K_s:
                stop_music()
            if event.key == pygame.K_n:
                next_song()
            if event.key == pygame.K_b:
                previous_song()
        
    # заливаем экран
    screen.fill("white")

    pygame.display.flip()
    clock.tick(60)

pygame.quit()