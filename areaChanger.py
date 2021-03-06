#!/usr/bin/env python3.5

from pymouse import PyMouseEvent
from pymouse import PyMouse
import subprocess as tux
import sys
import shlex
import time


# Given a position on the screen this functions the wacom area on (mouse_x, mouse_y)
def change_wacom_position(mouse_x, mouse_y):
    wacom_pos_x = int(
        -int(wacom_x) * int(mouse_x) * divisor * aspectRatioCorrection / displayResolution_X + int(wacom_x) / 2)
    wacom_pos_y = int(-int(wacom_y) * int(mouse_y) * divisor / displayResolution_Y + int(wacom_y) / 2)

    wacom_weigh = int(divisor * aspectRatioCorrection * int(wacom_x))
    wacom_height = int(divisor * int(wacom_y))

    tux.call(shlex.split("xsetwacom --set " + wacomID + " area " + str(wacom_pos_x) + " " + str(wacom_pos_y) + " " \
                         + str(wacom_pos_x + wacom_weigh) + " " + str(wacom_pos_y + wacom_height)))


lastClick = 0
def is_double_click():
    global lastClick
    new_click = time.time()
    delta = new_click - lastClick
    lastClick = new_click
    if delta < 0.6:
        return True
    else:
        return False


class MouseListener(PyMouseEvent):
    def __init__(self):
        PyMouseEvent.__init__(self)

    def click(self, x, y, button, press):
        if press and button == 3 and is_double_click():
            time.sleep(0.2)
            change_wacom_position(x, y)


if len(sys.argv) != 3:
    print("./areaChanger.py < wacom tablet id > < division ratio of the screen >")
    exit(1)

# It's the global party now :)

wacomID = sys.argv[1]
divisor = float(sys.argv[2])

mouse = PyMouse()
displayResolution_X, displayResolution_Y = mouse.screen_size()

tux.call(shlex.split("xsetwacom --set " + wacomID + " ResetArea"))

_, _, wacom_x, wacom_y = tux.getoutput(" xsetwacom --get " + wacomID + " area").split(" ")
aspectRatioCorrection = (float(displayResolution_X) / float(displayResolution_Y)) / (float(wacom_x) / float(wacom_y))

C = MouseListener()
C.run()
