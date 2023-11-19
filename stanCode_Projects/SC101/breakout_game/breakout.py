"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

This is my version - Breakout Game!
It's not perfect, but it really took me a really long time, hope you like it!
"""

from campy.gui.events.timer import pause
from campy.graphics.gobjects import GLabel
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()
    lives = NUM_LIVES

    # Extension: create GLabel to demonstrate user's lives
    user_lives_label = GLabel("Lives remaining: " + str(lives))
    graphics.window.add(user_lives_label, x=graphics.window.width-user_lives_label.width, y=graphics.window.height-10)

    # Add the animation loop here!
    # dx = graphics.set_ball_x_velocity()
    # dy = graphics.set_ball_y_velocity()

    # ## initial velocities should be 0
    dx = graphics.get_vx()
    dy = graphics.get_vy()

    # Animation loop
    while True:
        # game over
        if lives == 0:
            graphics.window.remove(graphics.ball)
            graphics.window.add(graphics.user_loses_label, x=(graphics.window.width-graphics.user_loses_label.width)/2,
                                y=(graphics.window.height+graphics.user_loses_label.height)/2)
            break
        if graphics.controller and graphics.score != graphics.total_score:
            while True:
                if graphics.game_start:
                    graphics.game_start = False
                    graphics.set_ball_velocity()
                    dx = graphics.get_vx()
                    dy = graphics.get_vy()
                # move
                graphics.ball.move(dx, dy)
                # check
                if graphics.ball.x < 0 or graphics.ball.x + graphics.ball.width > graphics.window.width:
                    dx = -dx
                if graphics.ball.y < 0 or graphics.ball.y + graphics.ball.height > graphics.window.height:
                    dy = -dy
                # pause
                pause(FRAME_RATE)

                # set up reactions of the ball
                maybe_object1 = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y)
                maybe_object2 = graphics.window.get_object_at(graphics.ball.x + graphics.ball.width, graphics.ball.y)
                maybe_object3 = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y + graphics.ball.height)
                maybe_object4 = graphics.window.get_object_at(graphics.ball.x + graphics.ball.width,
                                                              graphics.ball.y + graphics.ball.height)
                if maybe_object1 is not None and maybe_object1 is not graphics.paddle and \
                        maybe_object1 is not graphics.score_label and maybe_object1 is not user_lives_label:
                    graphics.window.remove(maybe_object1)
                    dy = -dy
                    graphics.score += 1
                    graphics.score_label.text = "Your score: " + str(graphics.score) + " / " + str(graphics.total_score)
                elif maybe_object1 is graphics.paddle:
                    graphics.window.remove(graphics.ball)
                    graphics.window.add(graphics.ball, x=graphics.ball.x, y=graphics.paddle.y-graphics.ball.height-1)
                    dy = -dy
                elif maybe_object2 is not None and maybe_object2 is not graphics.paddle and \
                        maybe_object2 is not graphics.score_label and maybe_object2 is not user_lives_label:
                    graphics.window.remove(maybe_object2)
                    dy = -dy
                    graphics.score += 1
                    graphics.score_label.text = "Your score: " + str(graphics.score) + " / " + str(graphics.total_score)
                elif maybe_object2 is graphics.paddle:
                    graphics.window.remove(graphics.ball)
                    graphics.window.add(graphics.ball, x=graphics.ball.x, y=graphics.paddle.y-graphics.ball.height-1)
                    dy = -dy
                elif maybe_object3 is not None and maybe_object3 is not graphics.paddle and \
                        maybe_object3 is not graphics.score_label and maybe_object3 is not user_lives_label:
                    graphics.window.remove(maybe_object3)
                    dy = -dy
                    graphics.score += 1
                    graphics.score_label.text = "Your score: " + str(graphics.score) + " / " + str(graphics.total_score)
                elif maybe_object3 is graphics.paddle:
                    graphics.window.remove(graphics.ball)
                    graphics.window.add(graphics.ball, x=graphics.ball.x, y=graphics.paddle.y - graphics.ball.height-1)
                    dy = -dy
                elif maybe_object4 is not None and maybe_object4 is not graphics.paddle and \
                        maybe_object4 is not graphics.score_label and maybe_object4 is not user_lives_label:
                    graphics.window.remove(maybe_object4)
                    dy = -dy
                    graphics.score += 1
                    graphics.score_label.text = "Your score: " + str(graphics.score) + " / " + str(graphics.total_score)
                elif maybe_object4 is graphics.paddle:
                    graphics.window.remove(graphics.ball)
                    graphics.window.add(graphics.ball, x=graphics.ball.x, y=graphics.paddle.y - graphics.ball.height-1)
                    dy = -dy

                # user win the game
                if graphics.score == graphics.total_score:
                    graphics.window.add(graphics.user_wins_label,
                                        x=(graphics.window.width-graphics.user_wins_label.width) / 2,
                                        y=(graphics.window.height+graphics.user_wins_label.height) / 2)
                    break

                # game failed
                if graphics.ball.y > graphics.paddle.y + graphics.paddle.height:
                    graphics.reset_ball()
                    lives -= 1
                    user_lives_label.text = "Lives remaining: " + str(lives)
                    break
            graphics.controller = False
        pause(FRAME_RATE)


if __name__ == '__main__':
    main()
