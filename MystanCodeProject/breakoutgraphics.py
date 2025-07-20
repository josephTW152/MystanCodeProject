"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.
---------------------------
File: breakoutgraphics.py
Name: Joseph Chiu
---------------------------
This program plays a game called
"Breakout" in which players
controls a paddle to bounce a ball and break bricks,
while preventing the ball from falling off the bottom of the screen.
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
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels) 15
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)
        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.paddle.fill_color = 'black'
        self.set_paddle_position((self.window.width - self.paddle.width) / 2, self.window.height - PADDLE_OFFSET)
        self.window.add(self.paddle)

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius * 2, ball_radius * 2, x=(self.window.width - ball_radius * 2) / 2,
                          y=(self.window.height - ball_radius * 2) / 2)
        self.ball.filled = True
        self.ball.dx = 0
        self.ball.dy = 0
        self.window.add(self.ball)

        # Default initial velocity for the ball

        # Initialize our mouse listeners
        onmouseclicked(self.ball_click)
        onmousemoved(self.paddle_move)

        # Draw bricks
        self.bricks_count = 0
        for i in range(brick_cols):
            for j in range(brick_rows):
                x = i*(brick_width+brick_spacing)
                y = 50+j*(brick_height+brick_spacing)
                self.bricks = GRect(40, 15, x=x, y=y)
                self.bricks.filled = True
                if j == 0 or j == 1:
                    self.bricks.fill_color = 'Red'
                elif j == 2 or j == 3:
                    self.bricks.fill_color = 'Orange'
                elif j == 4 or j == 5:
                    self.bricks.fill_color = 'Yellow'
                elif j == 6 or j == 7:
                    self.bricks.fill_color = 'Green'
                else:
                    self.bricks.fill_color = 'Purple'
                self.window.add(self.bricks)
        self.bricks_count = brick_cols * brick_rows

    def get_bricks_count(self):
        return self.bricks_count

    def get_dx(self):
        return self.ball.dx

    def get_dy(self):
        return self.ball.dy

    def ball_not_in_window(self):
        ball_y_not_in_window = self.ball.y + BALL_RADIUS*2 > self.window.height
        return ball_y_not_in_window

    def set_ball_velocity(self):
        self.ball.dx = random.randint(1, MAX_X_SPEED)
        self.ball.dy = INITIAL_Y_SPEED
        if random.random() > 0.5:
            self.ball.dx = -self.ball.dx
        if random.random() > 0.5:
            self.ball.dy = -self.ball.dy

    def reset_ball(self):
        self.ball.x = (self.window.width - BALL_RADIUS * 2) / 2
        self.ball.y = (self.window.height - BALL_RADIUS * 2) / 2
        self.ball.dx = 0
        self.ball.dy = 0
        onmouseclicked(self.ball_click)

    def ball_click(self, event):
        if self.ball.dx == 0 and self.ball.dy == 0:
            self.set_ball_velocity()

    def paddle_move(self, event):
        if event.x <= self.paddle.width/2:
            x = 0
        elif event.x >= self.window.width-self.paddle.width:
            x = self.window.width-self.paddle.width
        else:
            x = event.x-self.paddle.width/2
        self.set_paddle_position(x, self.window.height-PADDLE_OFFSET)

    def set_paddle_position(self, x, y):
        self.paddle.x = x
        self.paddle.y = y
