import random
import os
accept = 1
while(accept):
	print "==============================================="
	print "||   CHAO MUNG BAN DEN VOI TRO CHOI XUC XAC  ||"
	print "==============================================="
	kq = random.randint(1,6)
	print "|                 =====                      |"
	print "|                 | %d |                      |" % kq
	print "|                 =====                      |"
	print "|           Ban duoc %d diem.                 |" % kq
	print "|    Ban co muon tiep tuc hay khong (y/n) ?  |"
	print "=============================================="
	ask = raw_input()
	if ask != 'Y' and ask != 'y':
		accept = 0
	os.system('cls')
print "              Good job ! GoodBye Bro!"
