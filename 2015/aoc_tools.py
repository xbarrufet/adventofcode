import re
from urllib.request import urlopen
from heapq import heapify, heappop, heappush


sampleFile="./dades/sample$$.txt"
dataFile = "./dades/input$$.txt"





def nums(s):
   m=re.findall(r"-?\d+",s)  
   return [int(x) for x in m]

def readFileAsString(day, prod=False):
    filename = sampleFile.replace("$$",str(day)) if not prod else dataFile.replace("$$",str(day))
    with open(filename) as file:
       return file.readline().rstrip()
   

def readFileAsList(day, prod=False):
    filename = sampleFile.replace("$$",str(day)) if not prod else dataFile.replace("$$",str(day))
    with open(filename) as file:
        lines = [line for line in file]
    return lines


def readFileAsCharMap(day,prod=False):
    filename = sampleFile.replace("$$",str(day)) if not prod else dataFile.replace("$$",str(day))
    with open(filename) as file:
        lines = [list(line.rstrip()) for line in file]
    return lines


def readFileAsNumMap(filename):
    with open(filename) as file:
        lines = [list(line.rstrip()) for line in file]
    lineInt = []   
    for line in lines:
        lineInt.append([int(x) for x in line])
    return lineInt


def readFileAsNumColumns(filename,numColums):
    res =[[]*numColums]
    with open(filename) as file:
       for line in file:
           cols = nums(line)
           for i in range(numColums):
               res[i].append(cols[i])
    return res
    

class Graph:
    def __init__(self, graph: dict = {}):
       self.graph = graph  # A dictionary for the adjacency list

    def add_edge(self, node1, node2, weight):
       if node1 not in self.graph:  # Check if the node is already added
           self.graph[node1] = {}  # If not, create the node
       self.graph[node1][node2] = weight  #
    
    def shortest_distances(self, source: str):
        # Initialize the values of all nodes with infinity
        distances = {node: float("inf") for node in self.graph}
        distances[source] = 0  # Set the source value to 0
        # Initialize a priority queue
        pq = [(0, source)]
        heapify(pq)

        # Create a set to hold visited nodes
        visited = set()
        while pq:  # While the priority queue isn't empty
            current_distance, current_node = heappop(pq)  # Get the node with the min distance
            if current_node in visited:
               continue  # Skip already visited nodes
            visited.add(current_node)  # Else, add the node to visited set
           
            for neighbor, weight in self.graph[current_node].items():
                # Calculate the distance from current_node to the neighbor
                tentative_distance = current_distance + weight
                if tentative_distance < distances[neighbor]:
                    distances[neighbor] = tentative_distance
                    heappush(pq, (tentative_distance, neighbor))

        return distances
    
    def shortest_distances_and_predecessors(self, source: str):
        # Initialize the values of all nodes with infinity
        distances = {node: float("inf") for node in self.graph}
        distances[source] = 0  # Set the source value to 0
        # Initialize a priority queue
        pq = [(0, source)]
        heapify(pq)

        # Create a set to hold visited nodes
        visited = set()
        while pq:  # While the priority queue isn't empty
            current_distance, current_node = heappop(pq)  # Get the node with the min distance
            if current_node in visited:
               continue  # Skip already visited nodes
            visited.add(current_node)  # Else, add the node to visited set
           
            for neighbor, weight in self.graph[current_node].items():
                # Calculate the distance from current_node to the neighbor
                tentative_distance = current_distance + weight
                if tentative_distance < distances[neighbor]:
                    distances[neighbor] = tentative_distance
                    heappush(pq, (tentative_distance, neighbor))
                    
        predecessors = {node: [] for node in self.graph}

        for node, distance in distances.items():
            for neighbor, weight in self.graph[node].items():
                if distances[neighbor] == distance + weight:
                    predecessors[neighbor] = node

        return distances, predecessors

    def minimalPath(self,origin, target, cost):
        if origin==target:
            return [[origin]]
        d = self.shortest_distances(origin)
        distance = d[target]
        childs=[]
        for neighbour in self.graph[origin].keys():
            neighbour_cost = self.graph[origin][neighbour]
            d = self.shortest_distances(neighbour)
            if d[target]==cost-neighbour_cost:
                childs.append((neighbour,d[target]))
        res=[]
        for (nc,dt) in childs:
            paths= self.minimalPath(nc,target,dt)
            for p in paths:
                res.append([origin]+p)
        return res
  