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
print(factorint(N))