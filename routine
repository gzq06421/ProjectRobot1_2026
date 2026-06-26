from tinybit import *

auto_path = [
    ("forward", 70, 2000),
    ("pivot_right", 70, 1000),
    ("forward", 40, 1500),
    ("pivot_left", 70, 1000),
    ("forward", 70, 2000),
    ("stop", 0, 0)
]

def run_path(path):
    for act, spd, t in path:
        if act == "forward":
            move_custom_speed(spd)
        elif act == "pivot_right":
            pivot_right()
        elif act == "pivot_left":
            pivot_left()
        sleep_ms(t)
    stop_car()

run_path(auto_path)
