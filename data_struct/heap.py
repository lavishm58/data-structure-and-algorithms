from ctypes import *

import math
class heap:
    def __init__(self,array,size,i):
        self.array=array
        self.size=size
        self.i= i+1
    def Parent(self):
        if self.i>1:
            return math.floor(self.i/2-1)
        else:
            print('root')   
    def Left(self):
        return 2*self.i-1
    def Right(self):
        return 2*self.i
    def arraysize(self):
        return len(array)
    def  pop(self):
        self.size-=1
        self.array=self.array[0:self.size+1]
        return self.array
    def show(self):
        for i in range(0,self.size):
            print(self.array[i]) 

def heapsize(ar,i):
    while(not(math.floor((len(ar)-1)/2)<i<=(len(ar)-1))):
        a=heap(ar,len(ar),i)
        if a.Left()<=len(ar)-1:
            q=a.Left()
        if a.Right()<=len(ar)-1: 
            q=max(q,a.Right())
        i=q
    if (i>(math.floor((len(ar)-1)/2))):
        q=i

    return q

array=c_int*10
ar=array(2,5,1,3,2,6,32,5,673,3)
a=array()
lb=len(ar)
'''b=heap(ar,len(ar),1)
b.pop()
print('x')
b.show()'''
def maxheap(ar,i,lb):
    a=heap(ar,lb,i)
    l=a.Left()
    r=a.Right()
    if l<=lb-1 and ar[l]>ar[i] and i<=math.floor((lb-1)/2):
        large=l
    else:
        large=i

    if r<=lb-1 and ar[r]>ar[large] and i<=math.floor((lb-1)/2):
        large=r
    if large!=i:        
        key=ar[i]
        ar[i]=ar[large]
        ar[large]=key    
        return maxheap(ar,large,lb)
        
    return ar
a=heap(ar,3,1)
print(maxheap(ar,2,lb))   

def build_heap_max(ar,lb):
    for i in range(math.floor((lb)/2),0,-1):
        maxheap(ar,i,lb)
    return ar 
#print(build_heap_max(ar)[0])      
for i in range(0,len(ar)): 
     print(build_heap_max(ar,lb)[i])
def finalheap(ar):
    lb=len(ar)
    arr=build_heap_max(ar,lb)
    for i in range(len(ar)-1,0,-1):
        key=arr[0]

        arr[0]=arr[i]
        arr[i]=key
        lb=lb-1    
        print('this')
        #for j in range(0,lb):
         #   print(arr[j])
        #print(ar[0])
        maxheap(arr,0,lb)
    return arr
'''a2=finalheap(ar)    
for i in range(0,len(ar)):
 print(a2[i])'''