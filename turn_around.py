from tinybit import *
import time

def turn_left_slow():
    motor_left.run(30)
    motor_right.run(100)

def turn_right_slow():
    motor_left.run(100)
    motor_right.run(30)

def pivot_left():
    motor_left.run(-80)
    motor_right.run(80)

def pivot_right():
    motor_left.run(80)
    motor_right.run(-80)

stop_car()
