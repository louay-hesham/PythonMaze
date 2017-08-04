import heapq
from Core.Node import Node

class Search(object):

    found = None

    def __init__(self, start_node, maze): #Search constructor
        self.maze = maze
        self.start_node = start_node
        self.ds = []
        self.prev_node = None
        self.mode = 0
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
        
        if self.mode == 2:
            self.__init_BFS()

    def __init_BFS(self):
        self.ds.append(self.start_node)
        self.visited[self.start_node.i][self.start_node.j][self.start_node.k] = True
        self.maze.reset_colors()

    def __next_BFS_step(self):
        if self.ds and Search.found == None:
            s = self.ds.pop(0)
            self.maze.print("(BFS mode) Visiting " + " " + str(s))
            self.maze.tile_color[s.i][s.j][s.k] = 2
            if self.prev_node != None:
                self.maze.tile_color[self.prev_node.i][self.prev_node.j][self.prev_node.k] = 3
            self.prev_node = s
            children = s.get_children_nodes()
            if not children:
                return 0
            for child in children:
                if self.visited[child.i][child.j][child.k] == False:
                    self.ds.append(child)
                    self.maze.tile_color[child.i][child.j][child.k] = 1
                    self.visited[child.i][child.j][child.k] = True
        elif Search.found != None:
            self.maze.solved = True
            self.maze.print("BFS cost is " + str(Search.found.get_path_cost()))
        else:
            self.maze.print("No Solution")

    def set_mode(self, mode):
        self.mode = mode
        self.__reset()

    def next_step(self):
        if self.mode == 2:
            self.__next_BFS_step()

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

                   