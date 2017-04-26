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


array=c_int*10
ar=array(2,5,1,3,2,6,32,5,673,3)
a=array()
lb=len(ar)
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
        
    return ar[0:lb]
#a=heap(ar,3)
#print(maxheap(ar,2))
def build_heap_max(ar,lb):
    for i in range(math.floor((lb)/2)-1,0,-1):
        maxheap(ar,i,lb)
    maxheap(ar,0,lb)    
    return ar        


def customresize(ar,new_size):
        clib=CDLL("libc.so.6")    
        smallar=(c_int*new_size).from_buffer(ar)
        clib.realloc(ar,len(smallar))
        if new_size>len(ar):
            for i in range(len(ar)-1,new_size-1):
                ar[i]=0
            new_size=len(ar)
        for i in range(0,new_size-1):
            #print(ar[i])
            smallar[i]=ar[i]
        del ar
        return smallar
ar=customresize(ar,lb)
for i in range(0,len(ar)):        
    print(customresize(ar,3)[i])

maxarray=build_heap_max(ar,lb)

class priority:
    def __init__(self,maxarray,lb):
        self.maxarray=maxarray
        self.lb=lb
    def heap_maximum(self):
        return self.maxarray[0]
    def extract_max(self):
        if(lb<1):
            print('error')

        key=self.maxarray[0]
        self.maxarray[0]=self.maxarray[self.lb-1]
        self.maxarray[self.lb-1]=key
        self.lb=self.lb-1
        self.maxarray=maxheap(self.maxarray,0,self.lb)
        return self.maxarray
    def heap_increase_key(self,key,i):
        if key<=self.maxarray[i]:
            print('key is smaller')
        self.maxarray[i]=key
        self.maxarray=maxheap(self.maxarray,0,self.lb)
        return self.maxarray
    def heap_insert(self,key):
        self.lb=self.lb+1
        self.maxarray=customresize(self.maxarray,self.lb)
        self.maxarray[self.lb-1]=-math.inf 
        heap_increase_key(key,self.lb-1)
        return self.maxarray  
x=priority(maxarray,lb)
#print(x.heap_insert(12))              

