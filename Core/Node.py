
class Node(object):

    queue = []

    def __init__(self, i, j, k, maze, parent):
        self.i = i;
        self.j = j;
        self.k = k;
        self.parent = parent
        self.n = maze.map[i][j][k];
        self.maze = maze;
        self.visited = [None] * maze.height
        for i in range(0,maze.height):
            self.visited[i] = [None] * maze.length
            for j in range(0, maze.length):
                self.visited[i][j] = [False] * maze.width

    def __str__(self):
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

    def __get_children_coordinates(self, i, j, k, steps):
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

    def get_path(self):
        parent_cost = 0
        if self.parent != None:
            parent_cost = self.parent.get_path()

        Node.queue.append(self)
        #print(self)
        if isinstance (self.n, int):
            cost = self.n
        elif self.n == 'E':
            cost = 0
        else:
            cost = 1
        return cost + parent_cost

from Core.Search import Search





