import math, matplotlib.pyplot as plt, numpy as np
%matplotlib inline

n = 2
pl = (1/2,1,2,3)
x = [x/100 for x in range(n*100+1)]
y = [[math.pow(x,p) for x in x] for p in pl]


for yi in y:
	plt.plot(x,yi)
plt.savefig('puissances.png', bbox_inches='tight')

###############################

plt.figure()

n = 10
pl = (2,3)
x = [x/100 for x in range(n*100+1)]
y = [[math.pow(x,p) for x in x] for p in pl]

two_p_x = [math.pow(2,x) for x in x]
plt.plot(x,y[0],x,y[1],x,two_p_x)
plt.savefig('expo.png', bbox_inches='tight')

