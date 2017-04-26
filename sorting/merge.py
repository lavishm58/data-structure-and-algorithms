import math
def split(a,p,r):
	if(p<r):
		q=math.floor((p+r)/2)	
		split(a,p,q)
		split(a,q+1,r)
		merge(a,p,q,r)
	return a	

def merge(a,p,q,r):
	n1=q-p+1
	n2=r-q
	print(n2)
	l=[]
	r=[]	
	for i in range(0,n1):
		l.append(a[i+p])
	for i in range(0,n2):
		r.append(a[i+q+1])
	#print(l)
	i=0
	j=0
	for k in range(p,r):
		if(l[i]<=r[j] and i!=len(a)-1):
			a[k]=l[i]
			i+=1		
		if(l[i]>r[j] and j!=len(a)-1):
			a[k]=r[j]
			j+=1	
a=[2,6,3,4,2,1,5,3,99,7,6,8]
print(a)			
print(split(a,0,len(a)-1))
