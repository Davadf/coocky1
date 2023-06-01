import time
import mouse
import pyautogui


def upgrade(number):
    if number == 5:
        pyautogui.moveTo(1629, 265)
        mouse.click("left")
        time.sleep(1)
        pyautogui.moveTo(559, 483)
        print("moved to upgrade")

    if number == 50:
        pyautogui.moveTo(1703, 377)
        mouse.click("left")
        time.sleep(1)
        pyautogui.moveTo(559, 483)
        print("moved to cursor")

    if number == 500:
        pyautogui.moveTo(1703, 439)
        mouse.click("left")
        time.sleep(1)
        pyautogui.moveTo(559, 483)
        print("moved to grandma")

    if number == 5000:
        pyautogui.moveTo(1703, 505)
        mouse.click("left")
        time.sleep(1)
        pyautogui.moveTo(559, 483)
        print("moved to farm")

