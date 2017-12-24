# Wacom area automatic changer

This script is a solution to the problem of the wacom awkward area on linux, specially for big screens,
 multiple screen or wide screens.

When it's running you just have to **double click the mid mouse button** to center the mapped area on the mouse position,
the area aspect ratio is automatically fixed, you only have to specify the part of the screen you want to use:
 
 ```commandline
    $ ./areaChanger <id wacom pen> <multiplier>
```

### How to use it

0. Install wacom drivers: I used ```xsetwacom``` on 0.26.0 version 
1. Install python the dependencies: 
 ```commandline
    $ apt-get install python-xlib
    
    $ pip install Xlib
    $ pip install pymouse
 ```
 2. Get the id of your wacom pen:
  ```commandline
    $ xsetwacom --list
       
    Wacom Intuos PT S Pen stylus    id: 8   type: STYLUS    
    Wacom Intuos PT S Finger touch  id: 9   type: TOUCH     
    Wacom Intuos PT S Pen eraser    id: 14  type: ERASER    
    Wacom Intuos PT S Finger pad    id: 15  type: PAD 
  ```
 3. Run the script, in this example I want the wacom area to occupy a fourth of the screen so the height multiplier
 should be x2 (the width is set automatically depending on the tablet aspect ratio)
 
 ```commandline
    $ ./areaChanger 8 2
```

 
