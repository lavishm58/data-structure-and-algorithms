from ctypes import *

class Node(object):
    def __init__(self, data=None, next_node=None,set_object = None):
        self.data = data
        self.next_node = next_node
        self.set_object = set_object

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_data(self,new_data):
        self.data = new_data

    def set_next(self,new_next):
        self.next_node = new_next

class disjoint_set(object):
    def __init__(self,head=None,tail=None):
        self.head = head
        self.tail = tail 

def make_set(new_node):
    new_set = disjoint_set(new_node,new_node)
    new_node.set_object = new_set
        
def find_set(x):
    return x.set_object.head
    
def union(u,v):
    u.tail.set_next(v.head)
    u.tail = v.tail
    t = v.head
    while t != None:
        t.set_object = u
        t = t.get_next()

class edge(object):
    def __init__(self,a=None,b=None,weight=None):
        self.a = a
        self.b = b
        self.w = weight
        
class graph(object):
    def __init__(self,vertices,edges):
        self.V = vertices
        self.E = edges