import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 21))

commands = ['USER gembol\r\n', 'PASS 1508\r\n', 'RNFR test\r\n', 'RNTO test2\r\n', 'QUIT\r\n']
i = 1

while True:
  try:
    respond = s.recv(1024).decode()
    print(respond.strip())
    if 'Goodbye' in respond:
      break

    s.send(commands[i-1].encode())
    i+=1

  except socket.error:
    s.close()
    break