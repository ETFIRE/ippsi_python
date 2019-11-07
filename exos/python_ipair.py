#!/usr/bin/python3

"""
def ipair(n):	
	if n % 2 == 0:
		print("pair")
	else:
		print("impair")
	return(n)

lundi == 1

n = int(input('taper un chiffre'))
print(ipair(n))
"""

from datetime import datetime

d = datetime.now()
print(d)
if d.day % 2:
	print('jour pair')
else:
	print('jour impair')


print('numero du jour', d.day)
print('numero du jour ' + str(d.day)+ ' bonne journée!')
