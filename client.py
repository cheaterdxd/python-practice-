import socket
s = socket.socket()
host = '192.168.1.6'
port = 1234

s.connect((host, port))
messrecv = s.recv(1024)
while messrecv:
	print messrecv
	messent = raw_input()
	s.send(messent)
	messrecv = s.recv(1024)
s.close()
