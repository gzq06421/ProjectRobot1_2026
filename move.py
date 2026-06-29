from tinybit import *
import time

def move_forward():
    motor_left.run(100)
    motor_right.run(100)

def move_backward():
    motor_left.run(-100)
    motor_right.run(-100)

def stop_car():
    motor_left.stop()
    motor_right.stop()
