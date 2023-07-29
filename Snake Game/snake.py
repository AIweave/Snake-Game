from turtle import Turtle

STARTPOSTS = [(0, 0), (-20, 0), (-40, 0)]  # pixel size is 20x20; on a grid, 0 = head, -40 = tail
DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:

    def __init__(self):
        self.snakebody = []
        self.createsnake()  # automatically put the snake together
        self.head = self.snakebody[0]

    def createsnake(self):  # snake entire body
        for positions in STARTPOSTS:  # was for squares in range(3):, but error pops after calling "extend()"
            self.snakepart(positions)  # for every position in STARTPOSTS, a snakepart will be created and put there

    def snakepart(self, positions):
        snake = Turtle("square")
        snake.color("white")
        snake.pu()
        snake.goto(positions)  # snakepart will be placed in the different positions assgined when looped in createsnake
        self.snakebody.append(snake)

    def extend(self):
        self.snakepart(self.snakebody[-1].position())  # add snakepart to the last position (head) of the snakebody
        # position() is a turtle method that will locate an items position, in this case, snakebody[-1] position

    def move(self):  # this will need to be called
        for segments in range(len(self.snakebody) - 1, 0, -1):  # start at the head, stop at tail, -1 steps to get there
            x = self.snakebody[segments - 1].xcor()  # locating the x.cor & ycor of the midsegment
            y = self.snakebody[segments - 1].ycor()
            self.snakebody[segments].goto(x=x, y=y)
            # snakebody starting at 2, the last segment which is -40 on a grid (tail)
            # starts at 2 because start= 2 in the range()
            # and is index 2 in the snakebody Listl; it will go to the midsegment
        self.head.fd(DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def reset(self):  # basically doing the "init" over again
        for seg in self.snakebody:  # call all the snake parts for command(s)
            seg.goto(1000, 1000)  # tells the old snake(s) to go off the screen to keep a clean game board
        self.snakebody.clear()  # all the "snakepart" will be deleted
        self.createsnake()  # recreate snake
        self.head = self.snakebody[0]  # identifying the head of the snake
