"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.
---------------------------
File: breakout.py
Name: Joseph Chiu
---------------------------
This program plays a game called
"Breakout" in which players
controls a paddle to bounce a ball and break bricks,
while preventing the ball from falling off the bottom of the screen.
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics
from campy.gui.events.mouse import onmouseclicked

FRAME_RATE = 100         # 100 frames per second
NUM_LIVES = 3			# Number of attempts

graphics = BreakoutGraphics()


def main():
    lives = NUM_LIVES
    # Add the animation loop here!
    bricks_remove = graphics.bricks_count
    while True:
        pause(FRAME_RATE)
        if graphics.ball_not_in_window():
            lives -= 1
            if lives > 0:
                graphics.reset_ball()
            else:
                break
        graphics.ball.move(graphics.get_dx(), graphics.get_dy())
        check_obj = True
        paddle_collision = False
        for i in [0, graphics.ball.width]:
            for j in [0, graphics.ball.height]:
                obj = graphics.window.get_object_at(graphics.ball.x+i, graphics.ball.y+j)
                if obj is not None:
                    check_obj = False
                    if obj == graphics.paddle:  # obj is paddle
                        if graphics.ball.y+graphics.ball.height/2 > graphics.paddle.y:
                            paddle_collision = True
                        else:
                            graphics.ball.dy = -graphics.ball.dy
                            graphics.ball.y = graphics.paddle.y-graphics.ball.height   # reset ball.y position
                    else:  # obj is brick,,remove it and bricks count minus 1
                        graphics.window.remove(obj)
                        graphics.ball.dy = -graphics.ball.dy
                        bricks_remove -= 1
                    break
            if check_obj is False:
                break

        # remove all bricks then game finish
        if bricks_remove == 0:
            graphics.reset_ball()
            break

        if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width >= graphics.window.width or paddle_collision:
            graphics.ball.dx = -graphics.ball.dx

        if graphics.ball.y <= 0 and not paddle_collision:
            graphics.ball.dy = -graphics.ball.dy


if __name__ == '__main__':
    main()
