config = {
    "width": 720,
    "height": 576,
    "fps": 60, # can use 30 fps instead
    "player_gun_zoom": 1,
    "dmg": {
        "yellow": 10,
        "beige": 4,
        "pink": 12,
    },
    "speed": {
        # if using 30 fps, choose
        "yellow": (5, 3), # (10, 5)
        "beige": (3, 3), # (2, 2)
        "pink": (2, 4), # (4, 8)
        "blue": (2, 4), # (4, 8)
    },
    "firerate": {
        "yellow": 3,
        "beige": 2,
        "pink": 5,
        "blue": -1,
    },
    "sound": {
        "yellow": 'sfx_yellow.wav',
        "beige": 'sfx_beige.wav',
        "pink": 'sfx_pink.wav',
    },
    "mute": False,
}

def get_size():
    return (config['width'], config['height'])

def set_size(width, height):
    config['width'] = width
    config['height'] = height

def get_fps():
    return config['fps']

def get_player_gun_z():
    return config['player_gun_zoom']

def set_player_gun_z(value):
    config['player_gun_zoom'] = value

def get_dmg(type):
    return config['dmg'][type]

def set_dmg_enemies(yellow, beige, pink):
    config['dmg']['yellow'] = yellow
    config['dmg']['beige'] = beige
    config['dmg']['pink'] = pink

def get_speed(type):
    return config['speed'][type]

def set_speed_enemies(yellow, beige, pink):
    config['speed']['yellow'] = yellow
    config['speed']['beige'] = beige
    config['speed']['pink'] = pink

def get_firerate(type):
    return config['firerate'][type]

def set_firerate(yellow, beige, pink):
    config['firerate']['yellow'] = yellow
    config['firerate']['beige'] = beige
    config['firerate']['pink'] = pink

def get_sound(type):
    return config['sound'][type]

def get_mute():
    return config['mute']

def set_mute(value):
    config['mute'] = value