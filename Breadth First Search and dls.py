# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 09:38:46 2024

@author: HP
"""
graph = {'A':['B','C'],
         'B':['D','E'],
          'D':['F'],
         'C':['G'],
         'G':['H','I'],
         'H':[],
         'I':[],
         'F':[],
         'E':[],
         }

visited = []
queue = []

def bfs(visited,graph,node):
    visited.append(node)
    queue.append(node)
    
    while queue:
        m=queue.pop(0)
        print(m,end=" ")
        
        for neighbour in graph[m]:
            if neighbour not in visited :
                visited.append(neighbour)
                queue.append(neighbour)
                
print("Breadth first search traversal is :")
bfs(visited,graph,'A')
print(" ")


def dls(start,goal,path,level,maxD,graph):
    print("current level is:",level)
    print("starting node is",start)
    print("search is performed for:",goal)
    if start == goal:
        print("path is available")
        return path
    print("path is not available")
    
    if level == maxD:
        print("maximum limit is acieved")
        return False
    print("nExpanding the current node:")
    
    for child in graph[start]:
        path.append(child)
        
        if dls(child,goal,path,level+1,maxD,graph):
            return path
        path.pop()
    return False


start = input("Enter the starting point:")
goal = input("Enter node to be searched:")
maxD = int(input("Enter maxm depth"))
path=[start]
level = 0
res = dls(start,goal,path,level,maxD,graph)
if res:
    print("path to reach goal is:",res)
else:
    print("there is no path to reach goal")
            
        
               
        
        
        
        
        
        
        
        
        
        
        