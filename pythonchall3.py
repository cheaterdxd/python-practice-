 # -*- coding: utf-8 -*-
print '''
==========================================================
=      CHUONG TRINH DEM SO LAN XUAT HIEN CUA KI TU       =
=                   MADE BY: LE THANH TUAN               =
==========================================================
'''
thoat = 1
while thoat == 1:
	print "1. Load file"
	print "2. Nhap chuoi."
	print "3. Thoat."
	print " YOUR CHOICE"
	choice = raw_input()
	while (choice.isdigit() == False) or int(choice) < 0 or int(choice) > 3:
		print "Bro da nhap sai, vui long nhap lai."
		choice = raw_input()
	if choice == '2':
		print "Nhap chuoi muon dem:"
		inputString = raw_input()
	if choice == '1':
		inputfile = raw_input("Nhap duong dan cua file: ")
		while inputfile == '':
			print "Vui long nhap duong dan nao bro !"
			inputfile = raw_input("Nhap duong dan cua file: ")
		inputString = ''.join([line.rstrip() for line in open(inputfile)])
		diction = {}
		for c in inputString: 
			diction[c] = diction.get(c, 0) + 1
		for char in diction:
			print "{ %c : %d }" % (char , diction[char])
		print "====================================================="
	if choice == '3':
		print """
		==============================
		=  Cam on da su dung dich vu =
		==============================
		"""
		thoat = 0 