# uforama!
Shoot 'em up (Bullet Hell) + Tower Defense made with PyGame

## Gamers:

Hey! So glad you found this. 
It's a game built from scratch in the Python Language, is fun as heck and has plenty of slow-mo, exploding rockets, mines, and more powerups and enemies than a conventional indie dev game.
I worked on this alone, so might be a little biased, but now you get to see my perspective, so enjoy!

#### How-To:

The player basically controls a cute green UFO around a map with a bunch of scenery, dynamic elements, good and bad towers, enemies floating about and regularly shooting at you.

Movement is with WASD, shooting is done with the left mouse button.

Starting out, defeat the first patrolling wave of enemies before their tower sinks into the ground. Hint - it moves only when a guard alien is near the tower shield. When you do, the green flag along the track on the bottom of the screen will move to the next wave point - indicating more spawning enemies. Also, you will see your player's tower start to enter from the top of the screen, so try to stay near it and it will move downwards. Once your base station is planted into the earth and you have defeating all the waves of enemies, the level is a win and you get redirected to the Main Menu.

### Lore:

The earth is under attack from many species of aliens, who believe it is best to eradicate all of life from earth and mine its resources than let it be slowly polluted by humans.

Leshy, the friendly UFO, however, still has hope and faith in mankind, so the player cannot let the other UFOs be the end of this beautiful planet. So strap in, because your one-alien-army is the only thing standing between total annhilation of this planet. 

The details on different enemies and powerups can be found in-game.

### Theme Relevance:

This game was made for a hackathon, and the theme in accordance to be followed was 'Space'. I think this game encompasses the theme very well. You have character elements from space as protagonists and antagonists - the UFOs, then the gameplay also employs associated stuff - lasers, floating enemy and player stations, rockets etc. Lastly, the lore is set outta space, too! You play as the defending alien, saving mankind from the terrible and powerful beings not from earth.

## DevLog:

This section is for the developers. Highlights my ~14 day journey to building this game.

### Challenges Faced:

* Never worked with PyGame before - had to start from scratch.
* PyGame has no rigid structure for the game flow.
* Using cameras in PyGame and moving them about a map.
* Working with rotations and scaling in PyGame
* Not event driven.
* No complex sprites.

### Corresponding Solutions:

* I had made small games in Javascript before, so that came in handy.
* I set up a screen structure like in an app with, transitions, a direction system for event making and flow control.
* I created a box camera module, following tutorials on the internet
* I had to do a lot of testing to grasp the concept of Rects and Surfaces, but in the end I had it working like I wanted - hence the awesome graphics!
* I implemented event handling as most do, but with strict categorization, timing, and delicate connections with the camera, director and screen modules.
* I tried out a bunch of different rendering methodologies in my custom camera, but in the end went with a traditional approach, using creative wrapper classes around inbuilt sprite classes and using the structure provided by PyGame beforehand.

## Installation:

Download this package from wherever the code is hosted.
A Python Virtual Environment is preferred, but not necessary.
Latest Python distributions will work best.

Install dependencies (only PyGame) with the command pip install -r ./requirements.txt or manually installing PyGame.

To run the game, please ensure dependencies are installed, there are no additional apps running, and that you have a mouse ;)
Then run the command py main.py or python main.py or python3 main.py. Whichever works.

The game has been tested running smoothly at 60FPS on Windows.
The testing device had high end processors and large RAM, so if it lags, then manually set the game to 30FPS in the config.py file and accordingly change a few more parameters there for better play experience.

The game can be resized from the Options Menu, which switches from between an SD and HD resolution, and can be muted and its difficulty toggled between easy and hard modes - which affect fire rates of enemies.

## Screenshots:

#### Third Combat Area - 
![3rd Level Map](https://i.ibb.co/V20X6xw/Screenshot-2022-06-12-215829.png)

#### Second Combat Area - 
![2nd Level Map](https://i.ibb.co/KqzpSjr/Screenshot-2022-06-12-220050.png)

#### First Combat Area - 
![1st Level Map](https://i.ibb.co/fCVnxXg/Screenshot-2022-06-12-220226.png)

## Video Links:

[Game UI](https://vimeo.com/719602849) and [Gameplay](https://vimeo.com/719602810)