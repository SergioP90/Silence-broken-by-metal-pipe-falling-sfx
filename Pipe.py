import tkinter.messagebox as msgbx
import time
import winsound
import random
import os, sys


def playSound():
    winsound.PlaySound(resourcePath("Media\pipe.wav"), winsound.SND_FILENAME)

    
def main():
    msgbx.showwarning("Pipe", "Pipe activated")
    while True:
        playSound()
        randomNumber = random.randint(1, 20)# 1 to 20 minutes
        time.sleep(randomNumber * 60)# x times * 60 seconds

            
def resourcePath(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
        
    return os.path.join(base_path, relative_path)

if __name__ == "__main__":
    main()
