import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 21))
respond = s.recv(1024).decode()
print(respond.strip())
s.send(b'QUIT\r\n')
s.close()