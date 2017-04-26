from ctypes import *

class que:
	def __init__(self,n):
		self.n=n
		a=c_int*self.n
		self.a=a()
		self.head=None
		self.tail=0
	def insert(self,key):
		if(self.head!=None and self.head!=self.n-1):
			self.head+=1
			self.a[self.head]=key
		elif(self.head==self.n-1):
			self.a[self.tail]=key
			self.tail=0
			self.head=self.tail

			print('n',self.head)
		else:
			self.head=0
			self.a[self.head]=key
		return self.a	
	def delete(self):
		if(self.head!=self.tail):	
			self.tail+=1
			self.a=self.a[self.tail:self.n]
		else:
			self.tail+=1
			self.head+=1
			self.a=self.a[self.tail:self.n]
		return self.a
	def first(self):
		return self.a[self.tail]		
	def show(self):
		for i in range(0,self.head):
			print(self.a[i])				
x=que(3)
print(x.n)
print('head',x.head)
x.insert(1)
print('head',x.head)
x.insert(2)
print('head',x.head)

x.show()
x.insert(3)
print('head',x.head)
x.show()
x.insert(4)
x.show()
x.delete()
x.show()