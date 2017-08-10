
class Node(object):

    path = []  #list to keep track of the path moved
    
    def __init__(self, i, j, k, maze, parent):  #Node constructor
        self.i = i;
        self.j = j;
        self.k = k;
        self.__parent = parent
        if parent == None:
            self.n = 'S'
        else:
            self.n = maze.map[i][j][k];
        self.__maze = maze;
        self.__visited = [None] * maze.height
        self.cost = 0
        for i in range(0,maze.height):
            self.__visited[i] = [None] * maze.length
            for j in range(0, maze.length):
                self.__visited[i][j] = [False] * maze.width

    def __str__(self):  #method to print node line
        return str(self.n) + ' at (' + str(self.i) + ', ' + str(self.j) + ', ' + str(self.k) + ')' 

    def __hash__(self):
        return hash( (self.i, self.j, self.k) )

    def __eq__(self, other): 
        if not isinstance(other, type(self)):
            return False
        return self.i == other.i and self.j == other.j and self.k == other.k 

    def __iter__(self):
        for attr in dir(Node):
            if not attr.startswith("__"):
                yield attr

    def __lt__(self, other):
        n_self = self.n
        if not isinstance(self.n, int):
            n_self = 1
        n_other = other.n
        if not isinstance(other.n, int):
            n_other = 1
        return n_self < n_other
 
    def __get_children_coordinates(self, i, j, k, steps):  #recursive method to return set of unvisited children nodes to a given node
        if self.__visited[i][j][k]:
            return

        if self.__maze.map[i][j][k] =='E':
            Search.found = Node(i,j,k, self.__maze, self)
            return

        self.__visited[i][j][k] = True
        if self.__maze.map[i][j][k] == '#':
            return

        if steps == 0:
            self.__visited[i][j][k] = False
            return {Node(i, j, k, self.__maze, self)}

        childrens = set()
        #right
        if (k + 1) != self.__maze.width:
            x = self.__get_children_coordinates(i, j, k + 1, steps - 1)
            if x is not None:
                childrens.update(x)
        #left
        if (k - 1) != -1:
            x = self.__get_children_coordinates(i, j, k - 1, steps - 1)
            if x is not None:
                childrens.update(x)
        #forward
        if (j + 1) != self.__maze.length:
            x = self.__get_children_coordinates(i, j + 1, k, steps - 1)
            if x is not None:
                childrens.update(x)
        #backwards
        if (j - 1) != -1:
            x = self.__get_children_coordinates(i, j - 1, k, steps - 1)
            if x is not None:
                childrens.update(x)
        #up
        if (i + 1) != self.__maze.height and self.__maze.map[i][j][k] == 'A' and self.__maze.map[i + 1][j][k] == 'A':
            x = self.__get_children_coordinates(i + 1, j, k, steps - 1)
            if x is not None:
                childrens.update(x)
        #down
        if (i - 1) != -1 and self.__maze.map[i][j][k] == 'A' and self.__maze.map[i - 1][j][k] == 'A':
            x = self.__get_children_coordinates(i - 1, j, k, steps - 1)
            if x is not None:
                childrens.update(x)

        self.__visited[i][j][k] = False
        return childrens

    def get_children_nodes(self):
        steps = 0
        if isinstance(self.n, int):
            steps = self.n;
        elif self.n == 'S' or self.n == 'A':
            steps = 1
        elif self.n == 'E':
            steps = 0

        return self.__get_children_coordinates(self.i, self.j, self.k, steps)

    def get_path_cost(self): #method to calculate the total cost of a path
        if self.cost != 0:
            return self.cost

        parent_cost = 0
        if self.__parent != None:
            parent_cost = self.__parent.get_path_cost()

        Node.path.append(self)
       
        if isinstance (self.n, int):
            cost = self.n
        elif self.n == 'E':
            cost = 0
        else:
            cost = 1
        self.cost = cost + parent_cost
        return self.cost

    def get_path(self):  
        if len(Node.path) == 0:
            self.get_path_cost()
        return Node.path

from Core.Search import Search





