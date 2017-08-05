import heapq
from Core.Node import Node
import math

class Search(object):

    found = None

    def __init__(self, start_node, end_node, maze): #Search constructor
        self.__maze = maze
        self.__start_node = start_node
        self.__end_node = end_node
        self.__ds = []
        self.__prev_node = None
        self.mode = 0
        self.__visited = [None] * maze.height
        for i in range(0,maze.height):
            self.__visited[i] = [None] * maze.length
            for j in range(0, maze.length):
                self.__visited[i][j] = [False] * maze.width

    def __reset(self): #method to reset the search
        Search.found = None
        Node.path = []
        self.__ds = []
        self.__start_node.cost = 0
        self.__prev_node = None
        self.__visited = [None] * self.__maze.height
        for i in range(0,self.__maze.height):
            self.__visited[i] = [None] * self.__maze.length
            for j in range(0, self.__maze.length):
                self.__visited[i][j] = [False] * self.__maze.width
        if self.mode == 1:
            self.__init_DFS()
        elif self.mode == 2:
            self.__init_BFS()
        elif self.mode == 3:
            self.__init_UCS()
        elif self.mode == 4 or self.mode == 5:
            self.__init_A_star()
        self.maze.reset_colors()

    def __init_DFS(self):
        self.__ds.append(self.__start_node)
        self.__maze.print("DFS mode")

    def __next_DFS_step(self):
        if self.__ds and Search.found == None:
            s = self.__ds.pop()
            self.__maze.print("(DFS mode) Visiting " + " " + str(s))
            self.__maze.tile_color[s.i][s.j][s.k] = 2
            if self.__prev_node != None:
                self.__maze.tile_color[self.__prev_node.i][self.__prev_node.j][self.__prev_node.k] = 3
            self.__prev_node = s
            if self.__visited[s.i][s.j][s.k] == False:
                    self.__visited[s.i][s.j][s.k] = True
                    children = s.get_children_nodes()
                    if not children:
                       return 0

                    for child in children:
                         if self.__visited[child.i][child.j][child.k] == False:
                            self.__ds.append(child)
                            self.__maze.tile_color[child.i][child.j][child.k] = 1
        elif Search.found != None:
            self.__maze.solved = True
            self.__maze.print("DFS cost is " + str(Search.found.get_path_cost()))
        else:
            self.__maze.print("No Solution")

    def __init_BFS(self):
        self.__ds.append(self.__start_node)
        self.__visited[self.__start_node.i][self.__start_node.j][self.__start_node.k] = True
        self.__maze.print("BFS mode")

    def __next_BFS_step(self):
        if self.__ds and Search.found == None:
            s = self.__ds.pop(0)
            self.__maze.print("(BFS mode) Visiting " + " " + str(s))
            self.__maze.tile_color[s.i][s.j][s.k] = 2
            if self.__prev_node != None:
                self.__maze.tile_color[self.__prev_node.i][self.__prev_node.j][self.__prev_node.k] = 3
            self.__prev_node = s
            children = s.get_children_nodes()
            if not children:
                return 0
            for child in children:
                if self.__visited[child.i][child.j][child.k] == False:
                    self.__ds.append(child)
                    self.__maze.tile_color[child.i][child.j][child.k] = 1
                    self.__visited[child.i][child.j][child.k] = True
        elif Search.found != None:
            self.__maze.solved = True
            self.__maze.print("BFS cost is " + str(Search.found.get_path_cost()))
        else:
            self.__maze.print("No Solution")

    def __init_UCS(self):
        self.__ds.append((0,self.__start_node))
        self.__visited[self.__start_node.i][self.__start_node.j][self.__start_node.k] = True
        self.__maze.print("UCS mode")

    def __next_UCS_step(self):
        if self.__ds and Search.found == None:
            s= heapq.heappop(self.__ds)
            self.__maze.print("(UCS mode) Visiting " + " " + str(s[1]))
            self.__maze.tile_color[s[1].i][s[1].j][s[1].k] = 2
            if self.__prev_node != None:
                self.__maze.tile_color[self.__prev_node.i][self.__prev_node.j][self.__prev_node.k] = 3
            self.__prev_node = s[1]
            if s[1].n != 'E':
                children = s[1].get_children_nodes()
                if not children:
                    return 0
                for child in children:
                    if self.__visited[child.i][child.j][child.k] == False:
                        self.__maze.tile_color[child.i][child.j][child.k] = 1
                        self.__visited[child.i][child.j][child.k] = True
                        if s[1].n == "A" or s[1].n == 'S' or s[1].n == 'E':
                            heapq.heappush(self.__ds,(s[0] + 1, child))
                        else:
                            heapq.heappush(self.__ds,(s[0] + s[1].n, child))
        elif Search.found != None:
            self.__maze.solved = True
            self.__maze.print("UCS cost is " + str(Search.found.get_path_cost()))
        else:
            self.__maze.print("No Solution")

    def __init_A_star(self):
        self.__ds.append((0,self.__start_node))
        self.__visited[self.__start_node.i][self.__start_node.j][self.__start_node.k] = True
        self.__maze.print("A* mode with " + ("Manhattan distance" if self.mode == 4 else "Euclidean distance"))

    def __next_A_star_step(self):
        if self.__ds and Search.found == None:
            s = min(self.__ds, key=lambda o:o[0] + self.__heuristic(o[1]))
            self.__ds.remove(s)

            self.__maze.print("(A* mode with " + ("Manhattan distance" if self.mode == 4 else "Euclidean distance") + ") Visiting " + " " + str(s[1]))
            self.__maze.tile_color[s[1].i][s[1].j][s[1].k] = 2
            if self.__prev_node != None:
                self.__maze.tile_color[self.__prev_node.i][self.__prev_node.j][self.__prev_node.k] = 3
            self.__prev_node = s[1]

            if s[1].n != 'E':
                children = s[1].get_children_nodes()
                if not children:
                    return 0
                for child in children:
                    if self.__visited[child.i][child.j][child.k] == False:
                        self.__maze.tile_color[child.i][child.j][child.k] = 1
                        self.__visited[child.i][child.j][child.k] = True
                        if s[1].n == "A" or s[1].n == 'S' or s[1].n == 'E':
                            heapq.heappush(self.__ds,(s[0] + 1, child))
                        else:
                            heapq.heappush(self.__ds,(s[0] + s[1].n, child))
        elif Search.found != None:
            self.__maze.solved = True
            self.__maze.print("A* with " + ("Manhattan distance" if self.mode == 4 else "Euclidean distance") + " cost is " + str(Search.found.get_path_cost()))
        else:
            self.__maze.print("No Solution")

                        else:
                            heapq.heappush(self.ds,(s[0] + s[1].n, child))
        elif Search.found != None:
            self.maze.solved = True
            self.maze.print("A* with " + ("Manhattan distance" if self.mode == 4 else "Euclidean distance") + " cost is " + str(Search.found.get_path_cost()))
        else:
            self.maze.print("No Solution")

    def __manhattan(self, n):
        return abs(n.i - self.__end_node.i) + abs(n.j - self.__end_node.j) + abs(n.k - self.__end_node.k)

    def __Euc(self, n):
        return math.sqrt(math.pow((n.i - self.__end_node.i),2) + math.pow((n.j -self.__end_node.j),2) + math.pow((n.k -self.__end_node.k),2))
    
    def __heuristic(self, n):
            return self.__manhattan(n) if self.mode == 4 else self.__Euc(n)

    def __get_path(self):     #method to return the path of the search
        Search.found.get_path_cost()
        return Search.found.get_path()


    def set_mode(self, mode):
        self.mode = mode
        self.__reset()

    def next_step(self):
        if self.mode == 1:
            self.__next_DFS_step()
        elif self.mode == 2:
            self.__next_BFS_step()
        elif self.mode == 3:
            self.__next_UCS_step()
        elif self.mode == 4 or self.mode == 5:
            self.__next_A_star_step()

    def get_path(self):     #method to return the path of the search
        Search.found.get_path_cost()
        return Search.found.get_path()

   
    # NOT NEEDED ANYMORE, sebtaha 3shan catherine met2olsh eny bamsa7 ay 7aga 2ala2iha f weshy :D
    # bas ana 3yz amsa7ha el sara7a

    def BFS(self):  #breadth first search: Traverses the search saves the path and prints the total cost
        self.__reset()
        self.__ds.append(self.__start_node)
        self.__visited[self.__start_node.i][self.__start_node.j][self.__start_node.k] = True
        while self.__ds and Search.found == None:
            s = self.__ds.pop(0)
            print(s)
            children = s.get_children_nodes()
            if not children:
                return 0
            for child in children:
                if self.__visited[child.i][child.j][child.k] == False:
                    self.__ds.append(child)
                    self.__visited[child.i][child.j][child.k] = True
        self.__maze.solved = True
        self.__maze.print("BFS cost is " + str(Search.found.get_path_cost()))

    def UCS(self):  #uniform cost search: Traverses the search and finds the minimum cost path 
        self.__reset()
        self.__ds.append((0,self.__start_node))
        self.__visited[self.__start_node.i][self.__start_node.j][self.__start_node.k] = True
        while self.__ds and Search.found == None:
            s= heapq.heappop(self.__ds)
            print(s[1])
            if s[1].n == 'E':
                break
            children = s[1].get_children_nodes()
            if not children:
                return 0
            for child in children:
                if self.__visited[child.i][child.j][child.k] == False:
                    self.__visited[child.i][child.j][child.k] = True
                    if s[1].n == "A" or s[1].n == 'S' or s[1].n == 'E':
                        heapq.heappush(self.__ds,(s[0] + 1, child))
                    else:
                        heapq.heappush(self.__ds,(s[0] + s[1].n, child))
        self.__maze.solved = True 
        self.__maze.print("UCS cost is " + str(Search.found.get_path_cost()))

    def DFS(self): #depth first search: Traverses the search saves the path and prints the total cost
        self.__reset()
        self.__ds.append(self.__start_node)
        while self.__ds and Search.found == None:
            s = self.__ds.pop()
            print(s)
            if self.__visited[s.i][s.j][s.k] == False:
                    self.__visited[s.i][s.j][s.k] = True
                    children = s.get_children_nodes()
                    if not children:
                       return 0

                    for child in children:
                         if self.__visited[child.i][child.j][child.k] == False:
                            self.__ds.append(child)
        self.__maze.solved = True
        self.__maze.print("DFS cost is " + str(Search.found.get_path_cost()))   

    def ASM(self):  
        self.__reset()
        self.__ds.append((0,self.__start_node))
        self.__visited[self.__start_node.i][self.__start_node.j][self.__start_node.k] = True
        while self.__ds and Search.found == None:
            s = min(self.__ds, key=lambda o:o[0] + self.__manhattan(o[1], self.__end_node))
            self.__ds.remove(s)
            #s= heapq.heappop(self.ds)
            print(s[1])
            if s[1].n == 'E':
                break
            children = s[1].get_children_nodes()
            if not children:
                return 0
            for child in children:
                if self.__visited[child.i][child.j][child.k] == False:
                    self.__visited[child.i][child.j][child.k] = True
                    if s[1].n == "A" or s[1].n == 'S' or s[1].n == 'E':
                        heapq.heappush(self.__ds,(s[0] + 1, child))
                    else:
                        heapq.heappush(self.__ds,(s[0] + s[1].n, child))
        self.__maze.solved = True 
        self.__maze.print("ASM cost is " + str(Search.found.get_path_cost())) 

    def ASE(self):   
        self.__reset()
        self.__ds.append((0,self.__start_node))
        self.__visited[self.__start_node.i][self.__start_node.j][self.__start_node.k] = True
        while self.__ds and Search.found == None:
            s = min(self.__ds, key=lambda o:o[0] + self.__Euc(o[1], self.__end_node))
            self.__ds.remove(s)
            #s= heapq.heappop(self.ds)
            print(s[1])
            if s[1].n == 'E':
                break
            children = s[1].get_children_nodes()
            if not children:
                return 0
            for child in children:
                if self.__visited[child.i][child.j][child.k] == False:
                    self.__visited[child.i][child.j][child.k] = True
                    if s[1].n == "A" or s[1].n == 'S' or s[1].n == 'E':
                        heapq.heappush(self.__ds,(s[0] + 1, child))
                    else:
                        heapq.heappush(self.__ds,(s[0] + s[1].n, child))
        self.__maze.solved = True 
        self.__maze.print("ASE cost is " + str(Search.found.get_path_cost())) 
        