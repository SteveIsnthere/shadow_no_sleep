import win32api, win32con
import time

x = 0
y = 0
timer = 60


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)


while True:
    click(x, y)
    time.sleep(timer)
