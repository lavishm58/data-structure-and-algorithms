
import math
import queue

class vertex(object):
    def __init__(self,name=None,d=None,pi=None):
        self.name = name
        self.d = d
        self.pi = pi

class edge(object):
    def __init__(self,a=None,b=None,weight=None):
        self.a = a
        self.b = b
        self.w = weight
        
class graph(object):
    def __init__(self,vertices,edges,adj):
        self.V = vertices
        self.E = edges
        self.adj = adj
def initialise(G,s):
    for v in G.V:
        v.d = math.inf
        v.pi = None
    s.d = 0

def relax(u,v,w):
    if v.d > u.d + w:
        v.d = u.d + w
        v.pi = u

def dijktras(G,s):
    initialise(G,s)
    S = []
    q = queue.PriorityQueue()
    for v in G.V:
        q.put((v.d,v.name))
    while True:
        if q.empty():
            break
        u = q.get()
        if u[1] in S:
            continue
        #print('!!',u[1])
        S.append(u[1])
        for e in G.adj[u[1]]:
            if e.b.d > e.a.d + e.w:
                e.b.d = e.a.d + e.w
                e.b.pi = e.a
                q.put((e.b.d,e.b.name))
                
def PRINT_PATH(G,s,v):
    if v==s:
        print(' ',s.name,' ',end='')
    elif v.pi == None:
        print('No path from',s.name,'to',v.name,'exist')
    else:
        PRINT_PATH(G,s,v.pi)
        print(' ',v.name,' ',end='')
        
names = ['a','b','c','d','e','f','g','h','i']

v= []
for i in range(5):
    temp = vertex(i)
    v.append(temp)
e = []
tempd = edge(v[0],v[1],10)
e.append(tempd)
tempd = edge(v[0],v[3],5)
e.append(tempd)
tempd = edge(v[1],v[2],1)
e.append(tempd)
tempd = edge(v[1],v[3],2)
e.append(tempd)
tempd = edge(v[2],v[4],4)
e.append(tempd)
tempd = edge(v[3],v[1],3)
e.append(tempd)
tempd = edge(v[3],v[2],9)
e.append(tempd)
tempd = edge(v[3],v[4],2)
e.append(tempd)
tempd = edge(v[4],v[0],7)
e.append(tempd)
tempd = edge(v[4],v[2],6)
e.append(tempd)


adj = [[e[0],e[1]],[e[2],e[3]],[e[4]],[e[5],e[6],e[7]],[e[8],e[9]]]
'''for i in range(len(e)):
    print('(',e[i].a.data,',',e[i].b.data,')')'''
G = graph(v,e,adj)
dijktras(G,v[0])
PRINT_PATH(G,v[0],v[2])