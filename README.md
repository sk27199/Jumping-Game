# Jumping-Game

This project is an jumping game I built using Python and Pygame. The player controls a Spiderman who must constantly jump over bombs while the score updates and increases everytime he does. The game ends when a collision occurs.

This project focuses more on logic, control flow and real time program behaviour rather than the visual design of the game.

# Why I Built This Project

I built this project to strengthen my understanding of how interactive programs work behind the scenes. I wanted to practice concepts such as real time loops, event handling, collision detection and managing different states within a program. 

This project helped me move beyond basic scripts and into building software that reacts continuosly to user input and system events.

# How the Game Works

When the game starts, the player presses a key to begin. The game then runs inside a continuous loop where:

* player input is checked
* obstacles are spawned at timed intervals
* positions are updated every frame
* collisions are detected
* the score is updated regularly

The game includes a start screen, an active gameplay state, and a screen at the end showing the end score, which helped me understand how larger programs are structured and controlled.

# Key Technical Concepts Used

The project demonstrates:

* real time game loops
* keyboard and mouse input handling
* timed events unding Pygame's event system collision detection using adjusted hitboxes
* randomised obstacle spawning
* score tracking using unique identifiers
* state management (start,playing,game over)
* modular functions to keep the code readable and organised

# Challenges and Learning Outcomes

One of the biggest challenge I faced was making the collision accurate as the image included a transparent background so that would mean that the collision would happen within the space between both characters. To combat this I adjusted hitboxes rather than relying on the image boundaries as I had kept changing the characters so the sizes of the images were different so adjusting hitboxes made more sense.

Another challenge I faced was ensuring the bombs are spawned at appropraite distances. I implemented spacing logic to prevent unfair overlaps and improve gameplay flow.

The project improved my problem solving skills and taught me how to debug logical issues in a larger codebase.

# Future Improvements

With more time and experience, I would:

* add music, sound effects and animations
* introduce difficulty scaling
* store high score
* improve accessibility and controls

These improvements would build on the exisiting logic without changing the core structure.

## Demo

![Gameplay Demo](pygame_demo.gif)


# How to run

```
pip install pygame
python mygame.py
```

