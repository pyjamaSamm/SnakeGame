from turtle import Turtle

# create a tuple of positions
SNAKE_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake_segments = []
        self.create_snake()
        self.head = self.snake_segments[0]

    def create_snake(self):
        for position in SNAKE_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        # this will add the segment at a particular position
        new_square = Turtle(shape="square")
        new_square.penup()
        new_square.color("white")
        new_square.goto(position)
        self.snake_segments.append(new_square)

    def extend(self):
        # will add new segment at the end of the snake as it eats
        # the end of the snake is the last position of the list snake.snake_segments
        self.add_segment(self.snake_segments[-1].position())

    def snake_move(self):
        for seg in range(len(self.snake_segments) - 1, 0, -1):
            # get the x coordinate of the segment before it
            new_x = self.snake_segments[seg - 1].xcor()
            # get the y coordinate of the segment before it
            new_y = self.snake_segments[seg - 1].ycor()
            # now pass the coordinates to the present segment so tht it goes to the place of the segment before it
            self.snake_segments[seg].goto(x=new_x, y=new_y)

        # need to mke the first segment move forward otherwise the entire thing will become static
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        # as snake cant move on along its way up while it is moving down...need to turn head and then go up
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)

    def reset(self):
        for seg in self.snake_segments:
            seg.goto(1000, 1000)

        # all segments added in the list will get cleared
        self.snake_segments.clear()

        # make the three segment snake again
        self.create_snake()
        self.head = self.snake_segments[0]
