# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import queue

class vertex(object):
    def __init__(self,name=None,color=None,dist=None,pred=None):
        self.name = name
        self.color = color
        self.d = dist
        self.pi = pred

class graph(object):
    def __init__(self,adj):
        self.adj = adj
        self.V = []
        for i in range(len(adj)):
            temp = vertex(i)
            self.V.append(temp)
def fi(q):
    if q.empty():
        return False
    else:
        return True
def BFS(G,s):
    for u in G.V:
        u.color = 'white'
        u.d = -1
        u.pi = None
    s.color = 'gray'
    s.d = 0
    s.pi = None
    q = queue.Queue()
    q.put(s)
    while True:
        u = q.get()
        for v in G.adj[u.name]:
            if G.V[v].color == 'white':
                G.V[v].color = 'grey'
                G.V[v].d = u.d + 1
                G.V[v].pi = u
                q.put(G.V[v])
        u.color = 'black'
        if q.empty():
            break
def PRINT_PATH(G,s,v):
    if v==s:
        print(' ',s.name,' ',end='')
    elif v.pi == None:
        print('No path from',s.name,'to',v.name,'exist')
    else:
        PRINT_PATH(G,s,v.pi)
        print(' ',v.name,' ',end='')
adj = []
#n = int(input("Enter no. of vertices: "))
V=[0,1,2,3,4]
adj=[]
adj=[[1,2],[0,2,3],[0,1,3],[1,4],[3]]
#for i in range(n):
#    adj.append(list(map(int,input().split())))
G = graph(adj)
BFS(G,G.V[0])
PRINT_PATH(G,G.V[0],G.V[4])



        
