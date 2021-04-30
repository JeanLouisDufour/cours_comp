import math
from sympy.ntheory import isprime, factorint

start = 12345678987654321
for i in range(0,1000,2):
	if isprime(start+i):
		break
p1 = start+i
print(p1)

start = 23456789876543212
for i in range(1,1000,2):
	if isprime(start+i):
		break
p2 = start+i
print(p2)

N = p1*p2
print(N)
print(isprime(N))
if False:
	print(factorint(N))

def L(n,a,c):
	"""
	"""
	ln = math.log(n)
	lln = math.log(ln)
	p = c * (ln**a) * (lln**(1-a))
	return math.exp(p)

def GNFS(n):
	"""
	"""
	return L(n, 1/3, (64/9)**(1/3))

for x in (3,10,100,1000,p1,N):
	print(f'{x} : {GNFS(x)}')

	