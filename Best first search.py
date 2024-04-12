## creating graph by adding edges to node
from queue import PriorityQueue
v = 14
graph = [[] for i in range(v)]  #creating list for each node

def addedge(x,y,cost):
    graph[x].append((y,cost))
    graph[y].append((x,cost))
    
# implemented using integers addedge(x,y,cost);
addedge(0, 1, 3)
addedge(0, 2, 6)
addedge(0, 3, 5)
addedge(1, 4, 9)
addedge(1, 5, 8)
addedge(2, 6, 12)
addedge(2, 7, 14)
addedge(3, 8, 7)
addedge(8, 9, 5)
addedge(8, 10, 6)
addedge(9, 11, 1)
addedge(9, 12, 10)
addedge(9, 13, 2)


# Function For Implementing Best First Search
# Gives output path having lowest cost
 
def best_first_search(actual_src,goal,n):
    visited = [False]*n
    pq = PriorityQueue()
    pq.put((0,actual_src))
    visited[actual_src]=True
    print("path is:")
    while pq.empty() == False:
        u = pq.get()[1]
        # displaying path having lowest cost
        print(u,"->",end=" ")
        if u == goal:
            break
        
        for v,c in graph[u]:
            if visited[v] == False:
                visited[v] = True
                pq.put((c,v))
                
    print()
        
    
    
start = 0;
goal = 8;  

best_first_search(start,goal,v)