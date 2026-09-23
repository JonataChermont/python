

import pygame
import time

pygame.mixer.init()

pygame.mixer.music.load("abertura_frieren.mp3")

while pygame.mixer.music.get_busy():
  time.sleep(1)
