

class Node(object):

    def __init__(self, i, j, k, maze):
        self.i = i;
        self.j = j;
        self.k = k;
        self.n = maze.map[i][j][k];
        self.maze = maze;
        self.visited = [None] * maze.height
        for i in range(0,maze.height):
            self.visited[i] = [None] * maze.length
            for j in range(0, maze.length):
                self.visited[i][j] = [False] * maze.width

    def __get_children_coordinates(self, i, j, k, steps):
        if self.visited[i][j][k]:
            return

        self.visited[i][j][k] = True
        if self.maze.map[i][j][k] == '#':
            return

        if steps == 0:
            location = Location(i, j, k)
            print(location)
            return {location}

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
        if (i + 1) != self.maze.height and self.maze.map[i][j][k] == 'A':
            x = self.__get_children_coordinates(i + 1, j, k, steps - 1)
            if x is not None:
                children_set.update(x)
        #down
        if (i - 1) != -1 and self.maze.map[i][j][k] == 'A':
            x = self.__get_children_coordinates(i - 1, j, k, steps - 1)
            if x is not None:
                children_set.update(x)

        return children_set


    def get_children_nodes(self):
        steps = 0
        if isinstance(self.n, int):
            steps = self.n;
        elif self.n == 'S' or self.n == 'A':
            steps = 1
        elif self.n == 'E':
            steps = 0
        
        children_locations = self.__get_children_coordinates(self.i, self.j, self.k, steps)
        children_nodes = list()
        for location in children_locations:
            children_nodes.append(location.get_node(self.maze))
        return children_nodes

class Location(object):
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k

    def __str__(self):
        return '(' + str(self.i) + ', ' + str(self.j) + ', ' + str(self.k) + ')' 

    def __hash__(self):
        return hash( (self.i, self.j, self.k) )

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return False
        return self.i == other.i and self.j == other.j and self.k == other.k 

    def __iter__(self):
        for attr in dir(Location):
            if not attr.startswith("__"):
                yield attr

    def get_node(self, maze):
        return Node(self.i, self.j, self.k, maze)




