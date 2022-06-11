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
}

def get_size():
    return (config['width'], config['height'])

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