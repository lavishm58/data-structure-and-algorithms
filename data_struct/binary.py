class node(object):
	def __init__(self,key=None,parent=None,left=None,right=None):
		self.key=key
		self.parent=parent
		self.left=left
		self.right=right
class bst:
	def __init__(self,root=None):
		self.root=root
	def insert(self,k):
		if self.root==None:
			self.root=node(key=k)
		else:
			x=self.root
			while x!=None:
				y=x
				if x.key>k:
					x=x.left	
				else:
					x=x.right
			if y.key>k:
				y.left=node(key=k,parent=y)
			else:
				y.right=node(key=k,parent=y)
	def search(self,x,k):
		x=self.root
		while x.key!=k and x.key!=None:
			if x.key>k:
				x=x.left
			else:
				x=x.right
			return x		
	def max(self):
		x=self.root
		while x.right!=None:
			x=x.right
		return x
	def min(self,x):
		x=self.root
		while x.left!=None:
			x=x.left
		return x
	def secessor(self,x):
		x=self.search(self.root,x)
		if x.right!=None:
			return self.min(x.right)					
		if x.parent.left==x:
			return x.parent
		while x.parent.right!=x and x.parent!=None:
			x=x.parent	
		if x.parent==None:
			return self.root	

		else:
			print('no predecessor')
b=bst()
b.insert(1)						
b.insert(2)
print(b.secessor(2).key)
