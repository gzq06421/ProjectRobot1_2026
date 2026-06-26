from tinybit import *

def move_custom_speed(speed):
    if -100 <= speed <= 100:
        motor_left.run(speed)
        motor_right.run(speed)
    else:
        stop_car()

move_custom_speed(40)
sleep_ms(2000)

move_custom_speed(100)
sleep_ms(2000)
stop_car()
