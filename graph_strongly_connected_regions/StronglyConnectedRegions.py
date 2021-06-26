#This code is contributed by Neelam Yadav

from collections import defaultdict

#This class represents a directed graph using adjacency list representation
class Graph:
    def __init__(self,vertices):
        self.V= vertices
        self.graph = defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)

    def DFSUtil(self,v,visited):
        visited[v]= True
        #print(self.nodeName[v]+' ', end='')
        print(str(v)+' ', end='')
        for i in self.graph[v]:
            if visited[i]==False:
                self.DFSUtil(i,visited)

    def fillOrder(self,v,visited, stack):
        visited[v]= True
        for i in self.graph[v]:
            if visited[i]==False:
                self.fillOrder(i, visited, stack)
        stack = stack.append(v)

    def getTranspose(self):
        g = Graph(self.V)
        for i in self.graph:
            for j in self.graph[i]:
                g.addEdge(j,i)
        return g

    def printSCCs(self):
        stack = []
        visited =[False]*(self.V)
        for i in range(self.V):
            if visited[i]==False:
                self.fillOrder(i, visited, stack)
        gr = self.getTranspose()
        visited =[False]*(self.V)
        while stack:
            i = stack.pop()
            if visited[i]==False:
                gr.DFSUtil(i, visited)
                print("")

# Create a graph given in the above diagram



g = [
    [0,2,0,6,0,0,0,0,6,7],
    [0,0,4,7,2,0,0,0,0,0],
    [0,0,0,0,2,0,0,0,0,0],
    [0,0,1,0,1,0,0,5,0,0],
    [0,0,0,0,0,2,0,0,0,0],
    [5,3,0,0,0,0,0,0,0,0],
    [0,2,3,0,0,0,0,0,7,0],
    [0,0,0,0,0,0,1,0,4,0],
    [0,0,4,0,0,0,0,0,0,2],
    [0,0,0,0,0,0,0,0,0,0]
]


r = Graph(len(g))
for i in range(0, len(g)):
    for j in range(0, len(g[i])):
        if g[i][j] != 0:
            r.addEdge(i, j)
r.printSCCs()