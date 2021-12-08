from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        # stores the score
        self.counting = 0
        # to hide the turtle figure
        self.hideturtle()
        with open("data.txt", mode="r") as data:
            self.high_score = int(data.read())

        self.goto(x=0, y=270)
        self.color("white")
        self.update_scoreboard()

    def update_scoreboard(self) -> """will update the scoreboard""":
        self.clear()
        self.write(f"score = {self.counting} highscore = {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.counting > self.high_score:
            self.high_score = self.counting
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.counting = 0
        self.update_scoreboard()

    def counter(self) -> """will return count of score""":
        self.counting += 1
        self.update_scoreboard()
