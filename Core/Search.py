
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

    def BFS(self):
        self.ds.append(self.start_node)
        self.visited[self.start_node.i][self.start_node.j][self.start_node.k] = True
        while self.ds and Search.found == None:
            s = self.ds.pop(0)
            print (s)
            children = s.get_children_nodes()
            for child in children:
                if self.visited[child.i][child.j][child.k] == False:
                    self.ds.append(child)
                    self.visited[child.i][child.j][child.k] = True
        print (Search.found)


