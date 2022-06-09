config = {
    "width": 720,
    "height": 576,
    "fps": 30,
    "draw_order": [
        'background',
        'bullets',
        'enemies',
        'player',
        'ui'
    ]
}

def get_size():
    return (config['width'], config['height'])

def get_fps():
    return config['fps']

def get_draw_order():
    return config['draw_order']