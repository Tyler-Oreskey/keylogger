# Import socket module
import socket            
 
s = socket.socket()        
 
port = 1236
 
# connect to the server on local computer
s.connect(('127.0.0.1', port))
 
# receive data from the server and decoding to get the string.
print (s.recv(1024).decode())

s.close() 