"""
File: bouncing_call.py
Name: Gloria
-------------------------
This program simulates a bouncing ball at (START_X, START_Y)
that has VX as x velocity and 0 as y velocity. Each bounce reduces
y velocity to REDUCE of itself.
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

# Global variable
count = 0
controller = False

window = GWindow(800, 500, title='bouncing_ball.py')


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    global controller, count             # define global variables at first
    ball = set_up_a_ball()
    onmouseclicked(switch)               # remove (), we don't add () while passing a function
    while True:
        if controller:                   # controller is a boolean(T/F), no need to use 'is'
            vy = 0                       # initialize vy before animation
            while True:
                if ball.x > window.width:
                    reset(ball)          # remove and add
                    break
                # move
                ball.move(VX, vy)
                # check
                if ball.x + ball.width <= window.width:
                    vy += GRAVITY
                if ball.y + ball.height >= window.height:
                    vy = -vy*REDUCE
                # pause
                pause(DELAY)
            controller = False           # in case users click while animating
            count += 1
        if count == 3:
            break
        pause(DELAY)


def reset(ball):
    window.remove(ball)
    window.add(ball, x=START_X, y=START_Y)


def set_up_a_ball():
    ball = GOval(SIZE, SIZE)
    ball.filled = True
    ball.fill_color = "black"
    window.add(ball, x=START_X, y=START_Y)
    return ball


def switch(mouse):
    global controller
    controller = True
    # return controller   # This function returns nothing because controller is global


if __name__ == "__main__":
    main()
