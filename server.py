import socket

s = socket.socket()
host = '192.168.1.6'
port = 1234
s.bind((host,port))

s.listen(5)
c, addr = s.accept()
print 'Got connection from', addr
c.send('Thank you for conecting')
messrecv = c.recv(1024)
while messrecv:
	print messrecv
	messsent = raw_input()
	c.send(messsent)
	messrecv = c.recv(1024)
c.close()