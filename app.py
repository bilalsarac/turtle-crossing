
import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

car_manager = CarManager()
player = Player()
score_board = Scoreboard()
screen.onkeypress(key="Up", fun=player.move_forward)


game_state = True
while game_state:
    time.sleep(score_board.game_speed)
    screen.update()
    number = random.randint(0,5)
    if number==0:
        car_manager = CarManager()
    
    car_manager.car_forward()
    for i in car_manager.get_cars():
        if player.distance(i) <20:
            score_board.game_over()
            game_state = False



    if player.check_finishline() == True:
        score_board.level_up()
        score_board.increase_game_speed()
        player.reset_level()
        car_manager.reset_level()




screen.exitonclick()