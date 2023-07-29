from turtle import Turtle

ALIGN = "center"
FONT = ('Courier', 25, 'normal')


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:  # open text module; save as data
            self.highscore = int(data.read())  # read & make data an int for scoring; save as highscore
        self.color("white")
        self.pu()
        self.goto(x=0, y=255)
        self.hideturtle()
        self.updatescore()

    def updatescore(self):
        self.clear()  # couldn't clear() before because there was a gameover function
        self.write(arg=f"Score: {self.score} High Score: {self.highscore}", align=ALIGN, font=FONT)

    def addpoint(self):
        self.score += 1
        self.clear()
        self.updatescore()

    def resetscore(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode="w") as data:  # open & allow to write content
                data.write(f"{self.highscore}")  # call module & function; call highscore and use that
        self.score = 0  # codes must be in certain order to get desired result
        self.updatescore()

    # def finalscore(self):
    #     self.goto(x=0, y=0)
    #     self.write(arg="Game Over", align="center", font=FONT)

