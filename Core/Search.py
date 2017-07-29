import heapq
from queue import PriorityQueue
from Core.Node import Node

class Search(object):

    found = None

    def __init__(self, start_node, maze):
        self.maze = maze
        self.start_node = start_node
        self.ds = []
        self.visited = [None] * maze.height
        for i in range(0,maze.height):
            self.visited[i] = [None] * maze.length
            for j in range(0, maze.length):
                self.visited[i][j] = [False] * maze.width

    def __reset(self):
        Search.found = None
        Node.path = []
        self.ds = []
        self.start_node.cost = 0
        self.visited = [None] * self.maze.height
        for i in range(0,self.maze.height):
            self.visited[i] = [None] * self.maze.length
            for j in range(0, self.maze.length):
                self.visited[i][j] = [False] * self.maze.width

    def get_path(self):
        Search.found.get_path_cost()
        return Search.found.get_path()

    def BFS(self):
        self.__reset()
        self.ds.append(self.start_node)
        self.visited[self.start_node.i][self.start_node.j][self.start_node.k] = True
        while self.ds and Search.found == None:
            s = self.ds.pop(0)
            children = s.get_children_nodes()
            if not children:
                
                return 0
            for child in children:
                if self.visited[child.i][child.j][child.k] == False:
                    self.ds.append(child)
                    self.visited[child.i][child.j][child.k] = True
        self.maze.solved = True
        self.maze.print("BFS cost is " + str(Search.found.get_path_cost()))

    def UCS(self):
        self.__reset()
        self.ds.append((0,self.start_node))
        self.visited[self.start_node.i][self.start_node.j][self.start_node.k] = True
        while self.ds and Search.found == None:
            s= heapq.heappop(self.ds)
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

    def DFS(self):
        self.__reset()
        self.ds.append(self.start_node)
        while self.ds and Search.found == None:
            s = self.ds.pop()
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

                   