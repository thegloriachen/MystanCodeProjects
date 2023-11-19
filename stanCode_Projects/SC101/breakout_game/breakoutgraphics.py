"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

This is my version - Breakout Game!
It's not perfect, but it really took me a really long time, hope you like it!
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Width of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        self.window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        self.window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=self.window_width, height=self.window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.paddle.fill_color = "black"
        self.window.add(self.paddle, x=(self.window_width-paddle_width)/2, y=self.window_height-paddle_offset)

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2)
        self.ball.filled = True
        self.ball.fill_color = "black"
        self.window.add(self.ball, x=(self.window_width-self.ball.width)/2, y=(self.window_height-self.ball.height)/2)

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0

        # Initialize our mouse listeners
        onmouseclicked(self.switch)
        onmousemoved(self.paddle_move)

        # Initialize switch
        self.controller = False             # to check if mouse has clicked or not
        self.game_start = False             # to check if the game has started or not

        # Draw bricks
        brick_x_position = 0
        brick_y_position = BRICK_OFFSET
        for i in range(int(BRICK_ROWS)):
            for j in range(BRICK_COLS):
                self.brick = GRect(BRICK_WIDTH, BRICK_HEIGHT)
                self.brick.filled = True
                self.brick.fill_color = "blue"
                self.brick.color = "blue"
                self.window.add(self.brick, x=brick_x_position, y=brick_y_position)
                brick_x_position = brick_x_position + BRICK_WIDTH + BRICK_SPACING
            brick_x_position = 0
            brick_y_position = brick_y_position + BRICK_HEIGHT + BRICK_SPACING

        # Extension: create GLabel for score
        self.total_score = BRICK_ROWS*BRICK_COLS
        self.score = 0
        self.score_label = GLabel("Your score: " + str(self.score) + " / " + str(self.total_score))
        self.window.add(self.score_label, x=0, y=self.window.height-10)

        # Extension: create GLabel when user wins
        self.user_wins_label = GLabel("You win !!!")
        self.user_wins_label.font = "-50"
        self.user_wins_label.color = "red"

        # Extension: create GLabel when user loses
        self.user_loses_label = GLabel("You lose :(")
        self.user_loses_label.font = "-50"
        self.user_loses_label.color = "gray"

    def paddle_move(self, event):
        self.window.add(self.paddle, x=event.x - self.paddle.width / 2, y=self.window.height - PADDLE_OFFSET)
        if event.x + self.paddle.width / 2 >= self.window.width:
            self.paddle.x = self.window.width - self.paddle.width
        if event.x - self.paddle.width / 2 <= 0:
            self.paddle.x = 0

    # ############## getter and setter need to be written in different methods ##################

    def set_ball_velocity(self):
        self.__dx = random.randint(1, MAX_X_SPEED)
        if random.random() > 0.5:
            self.__dx = -self.__dx
        self.__dy = INITIAL_Y_SPEED
        # increase the velocity
        if self.score >= 10:
            self.__dy = self.__dy * 1.5

    def get_vx(self):
        return self.__dx

    def get_vy(self):
        return self.__dy

    def reset_ball(self):
        self.window.remove(self.ball)
        self.window.add(self.ball, x=(self.window_width-self.ball.width)/2, y=(self.window_height-self.ball.height)/2)

    def switch(self, event):
        if not self.controller:
            self.controller = True
            self.game_start = True
