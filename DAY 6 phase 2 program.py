'''class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.key=key
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.key)
        inorder(root.right)
def insert(node,key):
    if node is None:
        return Node(key)
    if key < node.key:
        node.left=insert(node.left,key)
    else:
        node.right=insert(node.right,key)
    return node
def minvalNode(node):
    current=node
    while(current.left is not None):
        current=current.left
    return current
def deleteNode(root,key):
    if root is None:
        return root
    if key < root.key:
        root.left=deleteNode(root.left,key)
    elif(key>root.key):
        root.right=deleteNode(root.right,key)
    else:
        if root.left is None:
            temp=root.right
            root=None
            return temp
        elif root.right is None:
            temp=root.left
            root=None
            return temp
        temp=minvalNode(root.right)
        root.key=temp.key
        root.right=deleteNode(root.right,temp.key)
    return root

root=None
root=insert(root,50)
root=insert(root,30)
root=insert(root,20)
root=insert(root,40)
root=insert(root,70)
root=insert(root,60)
root=insert(root,80)
print("inorder traversal of given tree")
inorder(root)
print("\ndelete20")
root=deleteNode(root,20)
inorder(root)
print("\delete 30")
root=deleteNode(root,30)
inorder(root)
print("\delete 50")
root=deleteNode(root,50)
inorder(root)
#import dictionary from graph
from collections import defaultdict
graph=defaultdict(list)
def addEdge(graph,u,v):
    graph[u].append(v)
def generate_edges(graph):
    edges=[]
    for node in graph:
        for neighbour in graph[node]:
            edges.append((node,neighbour))
    return edges
addEdge(graph, 'a' , 'c' )
addEdge(graph, 'b' , 'c' )
addEdge(graph, 'b' , 'e' )
addEdge(graph, 'c' , 'd' )
addEdge(graph, 'c' , 'e' )
addEdge(graph, 'c' , 'a' )
addEdge(graph, 'c' , 'b' )
addEdge(graph, 'e' , 'b' )
addEdge(graph, 'd' , 'c' )
addEdge(graph, 'e' , 'c' )

print(generate_edges(graph))


class Graph(object):
    def __init__(self,size):
        self.adjMatrix=[]
        for i in range(size):
            self.adjMatrix.append([0 for i in range(size)])
        self.size=size
    def add_edge(self,v1,v2):
        if v1==v2:
            print("same vertex &d and %d" % (v1,v2))
        self.adjMatrix[v1][v2]=1
        self.adjMatrix[v2][v1]=1
  
    def print_matrix(self):
        for row in self.adjMatrix:
            for val in row:
                print('{:4}'.format(val))
            print
def main():
    g=Graph(5)
    g.add_edge(0,1)
    g.add_edge(0,2)
    g.add_edge(1,2)
    g.add_edge(2,0)
    g.add_edge(2,3)
    g.print_matrix()
if __name__=='__main__':
    main()
#BFS
graph={
    '5':['3','7'],
    '3':['2','4'],
    '7':['8'],
    '2':[],
    '4':['8'],
    '8':[]
}

visit=[]
queue=[]

def bfs (visit,graph,node):
    visit.append(node)
    queue.append(node)
    while queue:
        m=queue.pop(0)
        print(m,end=" ")
        for neighbour in graph[m]:
            if neighbour not in visit:
                visit.append(neighbour)
                queue.append(neighbour)
bfs(visit,graph,'5')
'''

#DFS
graph={
    '5':['3','7'],
    '3':['2','4'],
    '7':['8'],
    '2':[],
    '4':['8'],
    '8':[]
}
visit=set()
def dfs (visit,graph,node):
    if node not in visit:
        print(node)
        visit.add(node)
        for neighbour in graph[node]:
            dfs(visit,graph,neighbour)
dfs(visit,graph,'5')
        




    
         
   
      
    
            
