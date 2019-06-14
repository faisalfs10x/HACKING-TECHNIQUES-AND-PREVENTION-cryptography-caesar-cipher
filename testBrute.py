# ni saya guna python 2.7
# WAN MOHAMMAD FAISAL BIN SAMMIO (B031720043)
# Soliseheaswar Sridaran (B031720019)

print "Hai, saya Faisal dan ini utk lab3"
mesejOrgtu = raw_input("masukkan text yg telah dicipherkan baris demi baris: ")

kombinasihuruf = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# loop pada semua kunci yg possible
for key in range(len(kombinasihuruf)):

# It is important to set translated to the blank string so that the
# previous iteration's value for translated is cleared.

	translated = ''

# The rest of the program is the same as the original Caesar program:
# run the encryption/decryption code on each symbol in the message

	for symbol in mesejOrgtu:
		if symbol in kombinasihuruf:
			num = kombinasihuruf.find(symbol) # dptkan nombor pd symbol
			num = num - key

# handle the wrap-around if num is 26 or larger or less than 0

			if num < 0:
				num = num + len(kombinasihuruf)

# tambah nombor simbol tu pada hujung yg dah diterjemah

			translated = translated + kombinasihuruf[num]

		else:
# hanya tambah simbol tanpa encrypt atau decrypt

			translated = translated + symbol

#paparkan kunci yg dah di test sekali dgn decryption dia.
#kat sini kita kena cari sendiri text yang valueable atau ade makna meaningful.

	print('Key #%s: %s' % (key, translated))
