import math

class vertex(object):
	def __init__(self,name=None,pi=None,d=None):
		self.d=d
		self.pi=pi
		self.name=name

class edge(object):
	def __init__(self,a,b,weight):
		self.a=a
		self.b=b
		self.weight=weight

class graph(object):
	def __init__(self,V,E):
		self.E=E
		self.V=V


def initialize(G,s):
	for i in G.V:
		i.d=math.inf
		i.pi=None
	s.d=0

def relax(u,v,w):
	if v.d>u.d+w:
		v.d=u.d+w
		v.pi=u

def bellmanford(G,s):
	initialize(G,s)
	for i in range(len(G.V)-1):
		for e in G.E:
			relax(e.a,e.b,e.weight)

	for e in G.E:
		if e.b.d>e.a.d+e.weight:
			return False
	return True
	
def Print_path(G,u,v):
	if u==v:
		print(u.name)
	elif v.pi==None:
		print('Error')
	else:
		Print_path(G,u,v.pi)
		print(v.name)

names = ['a','b','c','d','e','f','g','h','i']

v= []
for i in range(5):
    temp = vertex(i)
    v.append(temp)
e = []
tempd = edge(v[0],v[1],6)
e.append(tempd)
tempd = edge(v[0],v[3],7)
e.append(tempd)
tempd = edge(v[3],v[4],9)
e.append(tempd)
tempd = edge(v[3],v[2],-3)
e.append(tempd)
tempd = edge(v[4],v[0],2)
e.append(tempd)
tempd = edge(v[4],v[2],7)
e.append(tempd)
tempd = edge(v[2],v[1],-2)
e.append(tempd)
tempd = edge(v[1],v[2],5)
e.append(tempd)
tempd = edge(v[1],v[3],8)
e.append(tempd)
tempd = edge(v[1],v[4],-4)
e.append(tempd)

'''for i in range(len(e)):
    print('(',e[i].a.data,',',e[i].b.data,')')'''
G = graph(v,e)
if bellmanford(G,v[0]):
    print('No -ve cycle')
else:
    print('-ve cycle')
Print_path(G,v[0],v[4])					 	

