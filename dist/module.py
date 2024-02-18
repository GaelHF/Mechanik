import os
import pygame

def play(sound_path): 
    pygame.mixer.init()
    pygame.mixer.music.load(sound_path)
    pygame.mixer.music.play()

def volume(chiffre):
    if chiffre >= 0 and chiffre <=100:
        pygame.mixer.music.set_volume(float(int(chiffre) / 100))

def get_directory_names(directory):
    directory_names = []
    for current_directory, subdirectories, files in os.walk(directory):
        for subdirectory in subdirectories:
            directory_names.append(os.path.join(current_directory, subdirectory))
    return directory_names

def welcome():
    os.system("cls")
    print("MECHANIK IS ACTIVATED !")