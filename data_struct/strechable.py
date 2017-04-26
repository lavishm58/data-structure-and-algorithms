from ctypes import *
import math
class strech:
	def __init__(self):
		array=c_int*1
		self.ar=array()
		self.curcap=0
		self.maxcap=1	
	def insert(self,key):
		#print(self.lb)
		if(self.maxcap==self.curcap):
			self.maxcap=2*self.maxcap
			array1=c_int*self.maxcap
			ar1=array1()
			for i in range(0,self.curcap):
				ar1[i]=self.ar[i]
			self.curcap=self.curcap+1
			ar1[self.curcap-1]=key
			self.ar=ar1
		else:
			self.curcap=self.curcap+1
			array1=c_int*self.curcap
			ar1=array1()
			for i in range(0,self.curcap):
				ar1[i]=self.ar[i]
			ar1[self.curcap-1]=key
			self.ar=ar1
		del ar1
		return self.ar
	def delete(self):
		self.curcap-=1
		if(self.curcap==self.maxcap/4):
			self.maxcap=self.maxcap/2
			array1=c_int*self.maxcap
			ar1=array1()	
			for i in range(0,self.curcap):
				ar1[i]=self.ar[i]
			self.ar=ar1
			del ar1
		else:	
			self.ar=self.ar[0:self.curcap]
		return self.ar		
	def show(self):
		for i in range(0,self.curcap):
			print(self.ar[i])		
x=strech()
x.insert(1)
x.show()
x.insert(2)
print(x.maxcap)
x.insert(3)
print(x.maxcap)