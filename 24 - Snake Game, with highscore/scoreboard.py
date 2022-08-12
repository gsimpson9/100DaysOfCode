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
        with open('high_score.txt') as f:
            self.highscore = int(f.read())
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f'Score:{self.score} High Score:{self.highscore}', move=False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open('high_score.txt', 'w') as f:
                score = f.write(str(self.score))
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
