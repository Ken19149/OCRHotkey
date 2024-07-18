import socket

s = socket.socket()

port = 4444

s.bind(("127.0.0.1", port))

s.listen(1)

while True:
    c, addr = s.accept()
    print ('Got connection from', addr )
 
    c.send(b'Thank you for connecting')
 
    c.close()