import random
import math
ar=[]
for i in range(0,15):
	ar.append(random.uniform(0,1))
ls=[]
for i in range(0,len(ar)):
	ls.append([])
for i in range(0,len(ar)):
	ls[math.floor(10*ar[i])].append(ar[i])


def insertion(ar):
	for i in range(0,len(ar)-1):
		for j in range(i+1,len(ar)):
			if(ar[j]<ar[i]):
				key=ar[j]
				ar[j]=ar[i]
				ar[i]=key
	return ar
ar=[]	
for i in range(0,len(ls)):
	insertion(ls[i])
	ar=ar+ls[i]
print(ar)	