import json
from pydub import AudioSegment
import os
while True:
    keyboard_name = input("Keyboard Name : ")
    os.mkdir(f"./audios/{keyboard_name}")
    with open(f"./sounds/{keyboard_name}/config.json", "r") as f:
        data = json.loads(f.read())
        
    audio = AudioSegment.from_ogg(f"./sounds/{keyboard_name}/{data['sound']}")
    
    defines = data["defines"]
    
    for i in range(3):
        if i == 0:
            key = 1
            fname = "key"
        elif i==1:
            key = 47
            fname = "big_key"
        else:
            key = 57
            fname = "space"
        
        time = defines[str(key)]
        segement = audio[int(time[0]):int(time[0]+time[1])]
        segement.export(f"./audios/{keyboard_name}/{fname}.ogg", format="ogg")