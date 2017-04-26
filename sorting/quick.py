import random 
def quicksort(list,p,r):
	if (p<r):
		q=partition(list,p,r)
		print(list	)
		quicksort(list,p,q-1)
		quicksort(list,q+1,r)
	return list
def partition(list,p,r):
	x=list[r]
	i=p-1
	for j in range(p,r):
		if(list[j]<=x):
			i=i+1
			key=list[i]
			list[i]=list[j]
			list[j]=key

			
	key=list[r]		
	list[r]=list[i+1]
	list[i+1]=key		
	return i+1
def randompartition(a,p,r):
	y=random.randrange(p,r)
	key=a[y]
	a[y]=a[r]
	a[r]=key
	return partition(a,p,r)
def randquick(a,p,r):
	if p<r:
		q=randompartition(a,p,r)
		print(list)
		randquick(a,p,q-1)
		randquick(a,q+1,r)
	return a
list=[2,8,7,1,3,5,6,4,4]
lb=len(list)
r=lb-1
p=0	
n=randquick(list,p,r)
print(n)

