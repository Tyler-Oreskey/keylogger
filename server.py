import socket

s = socket.socket()
print("Successfully created socket.")

# the port that the vm and host communicate over
port = 1236

s.bind(('', port))
print ("Socket binded to %s" %(port))

while True:
    # Establish connection with client.
  c, addr = s.accept()    
  print ('Got connection from', addr)
 
  # send message to client
  c.send('I can see you'.encode())
 
  # Close the connection with the client
  c.close()
  break