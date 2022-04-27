import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 21))

commands = ['USER gembol\r\n', 'PASS 1508\r\n', 'PASV\r\n', 'QUIT\r\n']
i = 1

while True:
  try:
    respond = s.recv(1024).decode()
    print(respond.strip())
    if 'Goodbye' in respond:
      break

    elif 'Entering Passive Mode' in respond:
      port = int(respond.split(',')[4]) * 256 + int(respond.split(',')[5].replace(')\r\n', ''))
      # print(port)
      s2.connect(('localhost', port))
      s.send(b'NLST\r\n')
      respond2 = s2.recv(1024).decode()
      print(respond2.strip())
      respond = s.recv(1024).decode()
      print(respond.strip())
      s2.close()

    s.send(commands[i-1].encode())
    i+=1

  except socket.error:
    s.close()
    break