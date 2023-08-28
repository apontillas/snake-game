from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 25, 'normal')





class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open('data.txt') as file:
            self.high_score = int(file.read())
        self.hideturtle()
        self.penup()
        self.sety(250)
        self.pencolor('white')
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)


    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()
        with open('data.txt', mode='w') as file:
            file.write(f'{self.high_score}')


    def inc_score(self):
        self.score += 1
        self.update_scoreboard()





