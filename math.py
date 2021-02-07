import subprocess
import sys
import pyautogui
import time
import pyperclip
import platform
from pynput import keyboard


def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])


install("pyautogui")
install("pyperclip")
install("pynput")


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
