import subprocess
import sys
import pyautogui
import time
import pyperclip
import platform
from pynput import keyboard


running = True
specialChar = False


def type(text: str):
    pyperclip.copy(text)
    if platform.system() == "Darwin":
        pyautogui.hotkey("command", "v")
    else:
        pyautogui.hotkey("ctrl", "v")


def on_press(key):
    # try:
    #     print('alphanumeric key {0} pressed'.format(
    #         key.char))
    # except AttributeError:
    #     print('special key {0} pressed'.format(
    #         key))
    pass


def on_release(key):
    global running, specialChar
    try:
        if key.char == '_':
            # Stop listener
            running = False
            return False

        if (key.char == '`'):
            specialChar = not specialChar

        if (key.char == 'a' and specialChar):
            pyautogui.press('backspace')
            type("∀")

        if (key.char == 't' and specialChar):
            pyautogui.press('backspace')
            type("∃")

        if (key.char == 'e' and specialChar):
            pyautogui.press('backspace')
            type("∈")

        if (key.char == '=' and specialChar):
            pyautogui.press('backspace')
            type("≡")

        if (key.char == '!' and specialChar):
            pyautogui.press('backspace')
            type("¬")

        if (key.char == 'u' and specialChar):
            pyautogui.press('backspace')
            type("∪")

        if (key.char == 'i' and specialChar):
            pyautogui.press('backspace')
            type("∩")

        if (key.char == 's' and specialChar):
            pyautogui.press('backspace')
            type("⊆")

        if (key.char == 'd' and specialChar):
            pyautogui.press('backspace')
            type("⊂")

        if (key.char == 'x' and specialChar):
            pyautogui.press('backspace')
            type("⊇")

        if (key.char == 'c' and specialChar):
            pyautogui.press('backspace')
            type("⊃")

        if (key.char == 'z' and specialChar):
            pyautogui.press('backspace')
            type("⊄")

        if (key.char == 'q' and specialChar):
            pyautogui.press('backspace')
            type("⊅")

        if (key.char == 'r' and specialChar):
            pyautogui.press('backspace')
            type("∉")

        if (key.char == 'o' and specialChar):
            pyautogui.press('backspace')
            type("∅")

        if (key.char == '-' and specialChar):
            pyautogui.press('backspace')
            type("⊖")

        if (key.char == 'p' and specialChar):
            pyautogui.press('backspace')
            type("∎")

        if (key.char == 'y' and specialChar):
            pyautogui.press('backspace')
            type("⊢")





    except AttributeError:
        pass


listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()


def maincode():
    global running
    print("\n\nPress ` - toggle character replacement\nPress _ to exit")
    while (running):
        time.sleep(1)


maincode()
