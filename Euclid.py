def Euclid(a,b): #a > b
	while 1:
		tmp = a%b
		if tmp ==0:
			print b
			break
		a = b
		b = tmp

Euclid(40,160)