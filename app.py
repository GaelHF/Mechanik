import tkinter as tk
import customtkinter as ctk
import keyboard
import pygame
import module
import json


directory = module.get_directory_names("./audios")
keyboards = []
current_keyboard = "eg-oreo"
current_keyboard_name = "EG-Oreo"

for dir in directory:
    with open(f"{dir}/config.json", "r") as f:
        data = json.loads(f.read())
    keyboards.append(str(data["name"]))



app = ctk.CTk()
app.geometry("500x200")
app.title("Mechanik - v1.0.0")
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
pygame.init() 
module.welcome()
def on_pressed(e):
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