from libs import extra

sound_library = {}
sound_paths = {
    "shoot": "sounds/shoot.wav",
    "explosion": "sounds/explosion.wav"
}

def play_sound(id:str):
    if not sound_library.get(id):
        sound_library[id] = extra.load_sound(sound_paths[id])

    sound_library[id].play()

def shoot():
    play_sound("shoot")

def explosion():
    play_sound("explosion")