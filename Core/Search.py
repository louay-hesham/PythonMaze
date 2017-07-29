<<<<<<< 355fcca10a9b9bf2864e86e60aff1f0cbe0d99a7
from Core.Node import Node
=======
>>>>>>> Revert "DFS and UCS"

class Search(object):

    found = None

    def __init__(self, start_node, maze):
        self.path_queue = []
        self.maze = maze
        self.start_node = start_node
        self.ds = []
        self.visited = [None] * maze.height
        for i in range(0,maze.height):
            self.visited[i] = [None] * maze.length
            for j in range(0, maze.length):
                self.visited[i][j] = [False] * maze.width

    def __get_path(self, node):
        if node.parent != None:
            self.__get_path(node.parent)
        self.path_queue.append(node)

    def BFS(self):
        Node.queue = []
        self.ds.append(self.start_node)
        self.visited[self.start_node.i][self.start_node.j][self.start_node.k] = True
        while self.ds and Search.found == None:
            s = self.ds.pop(0)
            children = s.get_children_nodes()
            for child in children:
                if self.visited[child.i][child.j][child.k] == False:
                    self.ds.append(child)
                    self.visited[child.i][child.j][child.k] = True
        print("Cost is " + str(Search.found.get_path()))
        

    def get_path(self):
        self.__get_path(Search.found)
        return self.path_queue


    def DFS(self):
        self.ds.append(self.start_node)
       # self.visited[self.start_node.i][self.start_node.j][self.start_node.k] = True
        while self.ds and Search.found == None:
            s = self.ds.pop()
            if self.visited[s.i][s.j][s.k] == False:
                    self.visited[s.i][s.j][s.k] = True
                    children = s.get_children_nodes()
                    for child in children:
                         if self.visited[child.i][child.j][child.k] == False:
                            self.ds.append(child)

        #print("hena")
        #print(self.visited)
        print("Cost is dfs " + str(Search.found.get_path()))
