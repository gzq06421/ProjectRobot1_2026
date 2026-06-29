from tinybit import *
import bluetooth

bluetooth.on()

while True:
    if bluetooth.any():
        cmd = bluetooth.read(1).decode()
        if cmd == "F":
            move_custom_speed(70)
        elif cmd == "B":
            move_custom_speed(-70)
        elif cmd == "L":
            turn_left_slow()
        elif cmd == "R":
            turn_right_slow()
        elif cmd == "S":
            stop_car()
