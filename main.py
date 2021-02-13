# Import stuff
import tkinter as tk
from tkinter import filedialog
import pygame

root = tk.Tk()
root.withdraw()

# Ask for the file of the person/thing you want to shot
file = filedialog.askopenfilename()

pygame.mixer.init()
pygame.init()
gunshot = pygame.mixer.Sound('gunshot.mp3')
# Draw an idiot
idiot = pygame.image.load(file)
print(idiot.get_rect().size)
screen = pygame.display.set_mode(idiot.get_rect().size, 0, 32)
screen.fill((255, 255, 255))
idiot.convert()
screen.blit(idiot, (10, 10))
pygame.display.flip()

# Run until the user asks to quit
# Also detect if mouse is pressed to shoot or if r is pressed to reset
running = True
bholeshow = False
keys = [False]
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                gunshot.play()
                bhole = pygame.image.load("hole.png")
                pos = pygame.mouse.get_pos()
                screen.blit(bhole, (pos))
        if pygame.key.get_pressed()[pygame.K_r] == 1:
            screen.fill((255, 255, 255))
            idiot = pygame.image.load(file)
            idiot.convert()
            screen.blit(idiot, (10, 10))
            pygame.display.flip()

    pygame.display.update()

# Done! Time to quit.
pygame.quit()