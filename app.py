import os
os.system("pip install customtkinter")
os.system("pip install pygame")
os.system("pip install requests")

import tkinter as tk
import customtkinter as ctk
import keyboard
import pygame
import json
import webbrowser

import update
import module


#Varibables
directory = module.get_directory_names("./audios")
keyboards = []
current_keyboard = "eg-oreo"
current_keyboard_name = "EG-Oreo"
current_key = 0

#APP
for dir in directory:
    with open(f"{dir}/config.json", "r") as f:
        data = json.loads(f.read())
    keyboards.append(str(data["name"]))



app = ctk.CTk()
app.geometry("500x250")
app.title(f"Mechanik - {update.current_version}")
app.iconbitmap("./assets/icon.ico")
ctk.set_appearance_mode("Dark")

current_keyboard_label = ctk.CTkLabel(master=app, text="Current Keyboard: " + current_keyboard_name, width=20)
current_keyboard_label.pack(side="top", padx=(10, 10), pady=(10, 10))

box_ctk = ctk.CTkComboBox(app, values=keyboards)
box_ctk.pack(side="top", padx=(20, 20), pady=(10, 10))

def change_keyboard():
    global current_keyboard
    global current_keyboard_name
    
    if box_ctk.get() == "NK Cream":
        current_keyboard = "nk-cream"
        current_keyboard_name = "NK Cream"
        
    elif box_ctk.get() == "EG Oreo":
        current_keyboard = "eg-oreo"
        current_keyboard_name = "EG Oreo"
        
    elif box_ctk.get() == "EG Crystal Purple":
        current_keyboard = "eg-crystal-purple"
        current_keyboard_name = "EG Crystal Purple"
        
    elif box_ctk.get() == "CherryMX Red PBT":
        current_keyboard = "cherrymx-red-pbt"
        current_keyboard_name = "CherryMX Red PBT"
        
    elif box_ctk.get() == "CherryMX Red ABS":
        current_keyboard = "cherrymx-red-abs"
        current_keyboard_name = "CherryMX Red ABS"
        
    elif box_ctk.get() == "CherryMX Brown PBT":
        current_keyboard = "cherrymx-brown-pbt"
        current_keyboard_name = "CherryMX Brown PBT"
        
    elif box_ctk.get() == "CherryMX Brown ABS":
        current_keyboard = "cherrymx-brown-abs"
        current_keyboard_name = "CherryMX Brown ABS"
        
    elif box_ctk.get() == "CherryMX Blue PBT":
        current_keyboard = "cherrymx-blue-pbt"
        current_keyboard_name = "CherryMX Blue PBT"
        
    elif box_ctk.get() == "CherryMX Blue ABS":
        current_keyboard = "cherrymx-blue-abs"
        current_keyboard_name = "CherryMX Blue ABS"
        
    elif box_ctk.get() == "CherryMX Black PBT":
        current_keyboard = "cherrymx-black-pbt"
        current_keyboard_name = "CherryMX Black PBT"
        
    elif box_ctk.get() == "CherryMX Black ABS":
        current_keyboard = "cherrymx-black-abs"
        current_keyboard_name = "CherryMX Black ABS"
    
    elif box_ctk.get() == "Panda":
        current_keyboard = "panda"
        current_keyboard_name = "Panda"
        
    elif box_ctk.get() == "Box Jade":
        current_keyboard = "boxjade"
        current_keyboard_name = "Box Jade"    
        
    current_keyboard_label.configure(text="Current Keyboard : " + current_keyboard_name)
    current_keyboard_label.pack(side="top", padx=(10, 10), pady=(10, 10))
change_button = ctk.CTkButton(app, text="Change Keyboard", command=change_keyboard).pack(padx=60, pady=3)


def volu(value):
    module.volume(value)

credit = ctk.CTkLabel(master=app, text="Volume : ", width=20)
credit.pack(side="top", padx=(10, 10), pady=(10, 10))

volume = ctk.CTkSlider(app, from_= 0, to= 100, command=volu)
volume.pack(side="top", padx=(10, 10), pady=(10, 10))


credit = ctk.CTkLabel(master=app, text="Made by: @GaelHF", width=20)
credit.pack(side="top", padx=(10, 10), pady=(10, 10))

if update.is_update_available():
    link_font = ctk.CTkFont(family="underline, bold", underline=True, weight="bold")
    new_version = ctk.CTkLabel(master=app, text=f"An update is available ! ({update.get_new_version()})", width=20, text_color="cyan", fg_color="#2E2E2E", corner_radius=15, font=link_font)
    new_version.bind("<Button-1>", lambda e:webbrowser.open_new_tab("https://github.com/GaelHF/Mechanik/releases/latest"))
    new_version.pack(side="top", padx=(10, 10), pady=(10, 10))
    link_font.configure(family="url_font")


pygame.init()
module.welcome()
def on_pressed(e):
    global current_key
    if not int(e.scan_code) == current_key:
        current_key = int(e.scan_code)
        if keyboard.is_pressed("ctrl") or keyboard.is_pressed("alt") or keyboard.is_pressed("shift") or keyboard.is_pressed("tab") or keyboard.is_pressed("enter") or keyboard.is_pressed("command") or keyboard.is_pressed("backspace") or keyboard.is_pressed("return"):
            module.play(f"./audios/{str(current_keyboard)}/big_key.ogg")
        elif keyboard.is_pressed("space"):
            module.play(f"./audios/{str(current_keyboard)}/space.ogg")
        else:
            module.play(f"./audios/{str(current_keyboard)}/key.ogg")
keyboard.on_press(on_pressed)
app.mainloop()
keyboard.wait()
pygame.quit()