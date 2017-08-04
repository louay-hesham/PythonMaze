import heapq
from Core.Node import Node
import math

class Search(object):

    found = None

    def __init__(self, start_node, end_node, maze): #Search constructor
        self.maze = maze
        self.start_node = start_node
        self.end_node = end_node
        self.ds = []
        self.visited = [None] * maze.height
        for i in range(0,maze.height):
            self.visited[i] = [None] * maze.length
            for j in range(0, maze.length):
                self.visited[i][j] = [False] * maze.width

    def __reset(self): #method to reset the search
        Search.found = None
        Node.path = []
        self.ds = []
        self.start_node.cost = 0
        self.visited = [None] * self.maze.height
        for i in range(0,self.maze.height):
            self.visited[i] = [None] * self.maze.length
            for j in range(0, self.maze.length):
                self.visited[i][j] = [False] * self.maze.width

    def get_path(self):     #method to return the path of the search
        Search.found.get_path_cost()
        return Search.found.get_path()

    def BFS(self):  #breadth first search: Traverses the search saves the path and prints the total cost
        self.__reset()
        self.ds.append(self.start_node)
        self.visited[self.start_node.i][self.start_node.j][self.start_node.k] = True
        while self.ds and Search.found == None:
            s = self.ds.pop(0)
            print(s)
            children = s.get_children_nodes()
            if not children:
                return 0
            for child in children:
                if self.visited[child.i][child.j][child.k] == False:
                    self.ds.append(child)
                    self.visited[child.i][child.j][child.k] = True
        self.maze.solved = True
        self.maze.print("BFS cost is " + str(Search.found.get_path_cost()))

    def UCS(self):  #uniform cost search: Traverses the search and finds the minimum cost path 
        self.__reset()
        self.ds.append((0,self.start_node))
        self.visited[self.start_node.i][self.start_node.j][self.start_node.k] = True
        while self.ds and Search.found == None:
            s= heapq.heappop(self.ds)
            print(s[1])
            if s[1].n == 'E':
                break
            children = s[1].get_children_nodes()
            if not children:
                return 0
            for child in children:
                if self.visited[child.i][child.j][child.k] == False:
                    self.visited[child.i][child.j][child.k] = True
                    if s[1].n == "A" or s[1].n == 'S' or s[1].n == 'E':
                        heapq.heappush(self.ds,(s[0] + 1, child))
                    else:
                        heapq.heappush(self.ds,(s[0] + s[1].n, child))
        self.maze.solved = True 
        self.maze.print("UCS cost is " + str(Search.found.get_path_cost()))

    def DFS(self): #depth first search: Traverses the search saves the path and prints the total cost
        self.__reset()
        self.ds.append(self.start_node)
        while self.ds and Search.found == None:
            s = self.ds.pop()
            print(s)
            if self.visited[s.i][s.j][s.k] == False:
                    self.visited[s.i][s.j][s.k] = True
                    children = s.get_children_nodes()
                    if not children:
                       return 0

                    for child in children:
                         if self.visited[child.i][child.j][child.k] == False:
                            self.ds.append(child)
        self.maze.solved = True
        self.maze.print("DFS cost is " + str(Search.found.get_path_cost()))
    def manhattan(self, n1, n2):
        return abs(n1.i - n2.i) + abs(n1.j -n2.j) + abs(n1.k -n2.k)
    def ASM(self):  
        self.__reset()
        self.ds.append((0,self.start_node))
        self.visited[self.start_node.i][self.start_node.j][self.start_node.k] = True
        while self.ds and Search.found == None:
            s = min(self.ds, key=lambda o:o[0] + self.manhattan(o[1], self.end_node))
            self.ds.remove(s)
            #s= heapq.heappop(self.ds)
            print(s[1])
            if s[1].n == 'E':
                break
            children = s[1].get_children_nodes()
            if not children:
                return 0
            for child in children:
                if self.visited[child.i][child.j][child.k] == False:
                    self.visited[child.i][child.j][child.k] = True
                    if s[1].n == "A" or s[1].n == 'S' or s[1].n == 'E':
                        heapq.heappush(self.ds,(s[0] + 1, child))
                    else:
                        heapq.heappush(self.ds,(s[0] + s[1].n, child))
        self.maze.solved = True 
        self.maze.print("ASM cost is " + str(Search.found.get_path_cost())) 
    def Euc(self, n1, n2):
        return math.sqrt(math.pow((n1.i - n2.i),2) + math.pow((n1.j -n2.j),2) + math.pow((n1.k -n2.k),2))    
    def ASE(self):   
        self.__reset()
        self.ds.append((0,self.start_node))
        self.visited[self.start_node.i][self.start_node.j][self.start_node.k] = True
        while self.ds and Search.found == None:
            s = min(self.ds, key=lambda o:o[0] + self.Euc(o[1], self.end_node))
            self.ds.remove(s)
            #s= heapq.heappop(self.ds)
            print(s[1])
            if s[1].n == 'E':
                break
            children = s[1].get_children_nodes()
            if not children:
                return 0
            for child in children:
                if self.visited[child.i][child.j][child.k] == False:
                    self.visited[child.i][child.j][child.k] = True
                    if s[1].n == "A" or s[1].n == 'S' or s[1].n == 'E':
                        heapq.heappush(self.ds,(s[0] + 1, child))
                    else:
                        heapq.heappush(self.ds,(s[0] + s[1].n, child))
        self.maze.solved = True 
        self.maze.print("ASE cost is " + str(Search.found.get_path_cost())) 
        