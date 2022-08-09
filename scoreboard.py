import random
from turtle import Turtle, colormode


FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("black")
        self.penup()
        self.game_speed = 0.1
        self.hideturtle()
        self.goto(-210,250)
        self.write(f"Level: {self.score}",align="center",font=FONT)
        
    def level_up(self):
        self.score += 1
        self.clear()
        self.write(f"Level: {self.score}",align="center",font=FONT)
    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", align="center",font=FONT)
    def increase_game_speed(self):
        self.game_speed *=0.9