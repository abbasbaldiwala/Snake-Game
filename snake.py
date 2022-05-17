from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
U = 90
D = 270
L = 180
R = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.tail = self.segments[-1]

    def create_snake(self):
        for positions in STARTING_POSITIONS:
            self.add_segment(positions)

    def add_segment(self, position):
        seg = Turtle("square")
        seg.color("white")
        seg.pu()
        seg.goto(position)
        self.segments.append(seg)

    def extend(self):
        self.add_segment(self.tail.position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() == D:
            pass
        else:
            self.head.seth(U)

    def down(self):
        if self.head.heading() == U:
            pass
        else:
            self.head.seth(D)

    def right(self):

        if self.head.heading() == L:
            pass
        else:
            self.head.seth(R)

    def left(self):

        if self.head.heading() == R:
            pass
        else:
            self.head.seth(L)

    def reset_snake(self):
        for seg in self.segments:
            seg.goto(10000, 10000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
        self.tail = self.segments[-1]

