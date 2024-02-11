import pygame
import os
import keyboard

pygame.init()

def play(sound_path): 
    pygame.mixer.init()
    pygame.mixer.music.load(sound_path)
    pygame.mixer.music.play()

def get_directory_names(directory):
    directory_names = []
    for current_directory, subdirectories, files in os.walk(directory):
        for subdirectory in subdirectories:
            directory_names.append(os.path.join(current_directory, subdirectory))
    return directory_names

def welcome():
    os.system("cls")
    print("MECHANIK IS ACTIVATED !")