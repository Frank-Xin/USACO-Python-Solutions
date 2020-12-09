'''
Problem: Moocast

Source: http://www.usaco.org/index.php?page=viewproblem2&cpid=668

Solution: Construct an adjacency list based on cow coordinates and power. Perform a
depth first search starting from every node while keeping track of the amount of
nodes visited. Return the maximum amount of nodes visited by a single node.
'''

import math

#input stuff :)
inp = open("moocast.in", "r")
out = open("moocast.out", "w")
N = int(inp.readline())

coordinates = []
power = []
adj = dict()
for i in range(N):
    adj[i] = set()

for i in range(N):
    x, y, p = map(int, inp.readline().split())
    coordinates.append((x, y))
    power.append(p)

#adding nodes to adjacency list if power allows
for i in range(len(coordinates)):
    for j in range(i+1, len(coordinates)):
        if (math.sqrt(math.pow((coordinates[i][0] - coordinates[j][0]), 2) + math.pow((coordinates[i][1] - coordinates[j][1]), 2)) <= power[i]):
            adj[i].add(j)
            #print("{} is connected to {}".format(coordinates[i], coordinates[j]))
        
        if (math.sqrt(math.pow((coordinates[i][0] - coordinates[j][0]), 2) + math.pow((coordinates[i][1] - coordinates[j][1]), 2)) <= power[j]):
            adj[j].add(i)
            #print("{} is connected to {}".format(coordinates[j], coordinates[i]))

def dfs(graph, visited, current_node):
    visited.add(current_node)
    for node in graph[current_node]:
        if (node not in visited):
            dfs(graph, visited, node)

highest = 0
#perform dfs on all nodes to see which one has the most connections
for i in range(N):
    visited = set()
    dfs(adj, visited, i)
    #print(visited)
    highest = max(highest, len(visited))

print(highest, file=out)
