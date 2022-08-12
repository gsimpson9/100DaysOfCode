from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier', 18, 'normal')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        ScoreBoard.penup(self)
        self.goto(x=0, y=270)
        self.score = 0
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f'Score:{self.score}', move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(x=0, y=0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()




