import mouse
import time
import keyboard
import pyautogui
import random
import upgrade

i = 0;
m = True;
r = random.randint(1, 500000)

while i < 2:
    time.sleep(1)
    i = i + 1;
    print(i)
else:
    while m == True:

        r = random.randint(1, 50000000)

        mouse.click("left")

        upgrade.upgrade(r)

        if keyboard.is_pressed("q"):
            print("q pressed, ending loop")
            m = False
            break
