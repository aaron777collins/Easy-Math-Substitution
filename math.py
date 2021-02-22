import subprocess
import sys
import pyautogui
import time
import pyperclip
import platform
import tkinter as tk
from pynput import keyboard

running = True
specialChar = False

pyautogui.PAUSE = 0


def pasteStr(text: str):

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
            pyautogui.press('backspace')

        if (key.char == 'a' and specialChar):
            pyautogui.press('backspace')
            pasteStr("∀")

        if (key.char == 't' and specialChar):
            pyautogui.press('backspace')
            pasteStr("∃")

        if (key.char == 'e' and specialChar):
            pyautogui.press('backspace')
            pasteStr("∈")

        if (key.char == '=' and specialChar):
            pyautogui.press('backspace')
            pasteStr("≡")

        if (key.char == '!' and specialChar):
            pyautogui.press('backspace')
            pasteStr("¬")

        if (key.char == 'u' and specialChar):
            pyautogui.press('backspace')
            pasteStr("∪")

        if (key.char == 'i' and specialChar):
            pyautogui.press('backspace')
            pasteStr("∩")

        if (key.char == 's' and specialChar):
            pyautogui.press('backspace')
            pasteStr("⊆")

        if (key.char == 'd' and specialChar):
            pyautogui.press('backspace')
            pasteStr("⊂")

        if (key.char == 'x' and specialChar):
            pyautogui.press('backspace')
            pasteStr("⊇")

        if (key.char == 'c' and specialChar):
            pyautogui.press('backspace')
            pasteStr("⊃")

        if (key.char == 'z' and specialChar):
            pyautogui.press('backspace')
            pasteStr("⊄")

        if (key.char == 'q' and specialChar):
            pyautogui.press('backspace')
            pasteStr("⊅")

        if (key.char == 'r' and specialChar):
            pyautogui.press('backspace')
            pasteStr("∉")

        if (key.char == 'o' and specialChar):
            pyautogui.press('backspace')
            pasteStr("∅")

        if (key.char == '-' and specialChar):
            pyautogui.press('backspace')
            pasteStr("⊖")

        if (key.char == 'p' and specialChar):
            pyautogui.press('backspace')
            pasteStr("∎")

        if (key.char == 'y' and specialChar):
            pyautogui.press('backspace')
            pasteStr("⊢")

        if (key.char == ']' and specialChar):
            pyautogui.press('backspace')
            pasteStr("≠")

        if (key.char == 'h' and specialChar):
            pyautogui.press('backspace')
            file = open("README.md", "r", encoding="utf-8")
            root = tk.Tk()
            root.title("Help - README.md")
            S = tk.Scrollbar(root)
            T = tk.Text(root, height=30, width=100)
            S.pack(side=tk.RIGHT, fill=tk.Y)
            T.pack(side=tk.LEFT, fill=tk.Y)
            S.config(command=T.yview)
            T.config(yscrollcommand=S.set)
            T.insert(tk.END, file.read())
            tk.mainloop()




    except AttributeError:
        pass


listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()


def maincode():
    global running
    print("\n\nPress ` to toggle character replacement\nPress h when character replacement is enabled for help\nPress _ to exit")
    while (running):
        time.sleep(1)


maincode()
