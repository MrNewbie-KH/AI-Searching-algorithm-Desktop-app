import json
from queue import PriorityQueue
import Data
import math
def get_real_distance(start , end ,data):
    R = 6371.0710
    x_cord_start,y_cord_start=data[start]
    x_cord_end,y_cord_end=data[end]
    rlat1 = x_cord_start * (math.pi/180)
    rlat2 = x_cord_end * (math.pi/180)
    difflat = rlat2-rlat1; 
    difflon = (y_cord_end-y_cord_start) * (math.pi/180)
    #Great-Circle-Distance Formula Used in Google Maps
    d = 2 * R * math.asin(math.sqrt(math.sin(difflat/2)*math.sin(difflat/2)+math.cos(rlat1)*math.cos(rlat2)*math.sin(difflon/2)*math.sin(difflon/2)))
    return d
def A_star(visited, queue, real_distance, graph, src, dist):
    parent={}
    parent[src]="non"
    queue.put((0, src,"non"))
    actual_dis = {}
    for item in graph :
        actual_dis[item]=0
    visited.append((src))
    while not queue.empty():
        node = queue.get()
        parent[node[1]]=node[2]
        #print((node[0])," ",node[1])
        visited.append(node[1])
        if(node[1]==dist):
            break
        for child in graph[node[1]]:
            if child not in visited:
                visited.append(child) 
                actual_dis[child] = actual_dis[node[1]] + graph[node[1]][child]
                queue.put(((actual_dis[child]+get_real_distance(child,src,real_distance)),child,node[1]))
    actual_path=[] 
    currNode=distnation
    while currNode != "non":
        actual_path.append(currNode)
        currNode=parent[currNode]
    actual_path.reverse()
    return actual_path
               
    # print("Total Cost = ",actual_dis["J"])


visited = []
queue = PriorityQueue()

Graph_js = Data.GRAPH 
real_distance =Data.Coordinates
source ="minuf"
distnation="tanta"
get_real_distance(source,distnation,real_distance)
A_star(visited, queue, real_distance, Graph_js, source,distnation)
