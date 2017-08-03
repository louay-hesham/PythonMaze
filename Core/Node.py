
class Node(object):

    path = []  #list to keep track of the path moved
    
    def __init__(self, i, j, k, maze, parent):  #Node constructor
        self.i = i;
        self.j = j;
        self.k = k;
        self.parent = parent
        if parent == None:
            self.n = 1
        else:
            self.n = maze.map[i][j][k];
        self.maze = maze;
        self.visited = [None] * maze.height
        self.cost = 0
        for i in range(0,maze.height):
            self.visited[i] = [None] * maze.length
            for j in range(0, maze.length):
                self.visited[i][j] = [False] * maze.width

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
        if self.visited[i][j][k]:
            return

        if self.maze.map[i][j][k] =='E':
            Search.found = Node(i,j,k, self.maze, self)
            return

        self.visited[i][j][k] = True
        if self.maze.map[i][j][k] == '#':
            return

        if steps == 0:
            self.visited[i][j][k] = False
            return {Node(i, j, k, self.maze, self)}

        children_set = set()
        #right
        if (k + 1) != self.maze.width:
            x = self.__get_children_coordinates(i, j, k + 1, steps - 1)
            if x is not None:
                children_set.update(x)
        #left
        if (k - 1) != -1:
            x = self.__get_children_coordinates(i, j, k - 1, steps - 1)
            if x is not None:
                children_set.update(x)
        #forward
        if (j + 1) != self.maze.length:
            x = self.__get_children_coordinates(i, j + 1, k, steps - 1)
            if x is not None:
                children_set.update(x)
        #backwards
        if (j - 1) != -1:
            x = self.__get_children_coordinates(i, j - 1, k, steps - 1)
            if x is not None:
                children_set.update(x)
        #up
        if (i + 1) != self.maze.height and self.maze.map[i][j][k] == 'A' and self.maze.map[i + 1][j][k] == 'A':
            x = self.__get_children_coordinates(i + 1, j, k, steps - 1)
            if x is not None:
                children_set.update(x)
        #down
        if (i - 1) != -1 and self.maze.map[i][j][k] == 'A' and self.maze.map[i - 1][j][k] == 'A':
            x = self.__get_children_coordinates(i - 1, j, k, steps - 1)
            if x is not None:
                children_set.update(x)

        self.visited[i][j][k] = False
        return children_set

    def get_children_nodes(self):
        steps = 0
        if isinstance(self.n, int):
            steps = self.n;
        elif self.n == 'S' or self.n == 'A':
            steps = 1
        elif self.n == 'E':
            steps = 0

        return list(self.__get_children_coordinates(self.i, self.j, self.k, steps))

    def get_path_cost(self): #method to calculate the total cost of a path
        if self.cost != 0:
            return self.cost

        parent_cost = 0
        if self.parent != None:
            parent_cost = self.parent.get_path_cost()

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





