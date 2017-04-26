from ctypes import *


class Node(object):
	def __init__(self, data=None, next_node=None ):
		self.data = data
		self.next_node = next_node

	def get_data(self):
		return self.data

	def get_next(self):
		return self.next_node

	def set_data(self,new_data):
		self.data = new_data

	def set_next(self,new_next):
		self.next_node = new_next

class linkedlist(object):
	def __init__(self,head=None):
		self.head = head

	def insert(self,data):
		new_node = Node(data)
		new_node.set_next(self.head)
		self.head = new_node

	def size(self):
		current = self.head
		count = 0
		while current:
			count = count + 1
			current = current.get_next()
		return count

	def search(self, x):
		current = self.head
		found = False
		while current and found is False:
			if current.get_data() == x:
				found = True
			else:
				current = current.get_next()
		if current is None:
			raise ValueError("Data Not Found!!")
		return current

	def delete(self,x):
		current = self.head
		previous = None
		found = False
		while current and found is False:
			if current.get_data() == x:
				found = True
			else:
				previous = current
				current = current.get_next()
		if current is None:
			ValueError("Data Not Found!!")
		if previous == None:
			self.head = current.get_next()
		else:
			previous.set_next(current.get_next())


class vertex(object):
    def __init__(self,name=None,color=None,start=None,finish=None,pred=None):
        self.name = name
        self.color = color
        self.d = start
        self.f = finish
        self.pi = pred

class graph(object):
    def __init__(self,adj):
        self.adj = adj
        self.V = []
        for i in range(len(adj)):
            temp = vertex(i)
            self.V.append(temp)

def DFS(G):
    for u in G.V:
        u.color = 'white'
        u.pi = None
    global time
    time = 0
    for u in G.V:
        if u.color == 'white':
            DFS_VISIT(G,u)
            
def DFS_VISIT(G,u):
    global time
    time = time + 1
    u.d = time
    print(u.name,'.d = ',u.d)
    u.color = 'gray'
    for v in G.adj[u.name]:
        if G.V[v].color == 'white':
            G.V[v].pi = u
            DFS_VISIT(G,G.V[v])
    u.color = 'black'
    time = time + 1
    u.f = time
    print(u.name,'.f = ',u.f)
    topo.insert(u.name)

topo = linkedlist()
time = 0
adj = []
'''n = int(input("Enter no. of vertices: "))
for i in range(n):
    adj.append(list(map(int,input().split())))'''
adj = [[1,3],[4],[5,4],[1],[],[5]]
G = graph(adj)
DFS(G)
a = topo.head

while a != None:
    print(a.data)
    a = a.get_next()
