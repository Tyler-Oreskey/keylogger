import socket


def client_program():
    # get the hostname
    port = 1236
    host = socket.gethostname()

    client_socket = socket.socket()
    client_socket.connect((host, 1236))  # connect to the server

    message = input(" -> ")  # take input

    while message.lower().strip() != 'bye':
        client_socket.send(message.encode())  # send message
        data = client_socket.recv(1024).decode()  # receive response

        print('Received from server: ' + data)  # show in terminal

        message = input(" -> ")  # again take input

    client_socket.close()  # close the connection


if __name__ == '__main__':
    client_program()