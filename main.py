import time

import pyautogui
import numpy as np

screenWidth, screenHeight = pyautogui.size()
moving_range = 1


def move_curser():
    new_velocity_vector = np.random.randint(-moving_range, moving_range, size=2)
    current_mouse_x, current_mouse_y = pyautogui.position()
    mouse_x = current_mouse_x / screenWidth
    mouse_y = current_mouse_y / screenHeight
    if mouse_x > 0.75:
        new_velocity_vector[0] = -abs(new_velocity_vector[0])
    elif mouse_x < 0.25:
        new_velocity_vector[0] = abs(new_velocity_vector[0])

    if mouse_y > 0.75:
        new_velocity_vector[1] = -abs(new_velocity_vector[1])
    elif mouse_y < 0.25:
        new_velocity_vector[1] = abs(new_velocity_vector[1])

    pyautogui.moveTo(current_mouse_x + new_velocity_vector[0], current_mouse_y + new_velocity_vector[1])


while True:
    move_curser()
    time.sleep(600)
