import subprocess
import sys

#Ensures pip is installed:
subprocess.check_call([sys.executable, "-m", "ensurepip", "--default-pip"])

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

install("pyautogui")
install("pyperclip")
install("pynput")
install("tk")
