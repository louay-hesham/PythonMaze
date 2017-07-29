import heapq
from queue import PriorityQueue
from Core.Node import Node

class Search(object):

    found = None

    def __init__(self, start_node, maze):
        self.maze = maze
        self.start_node = start_node
        self.ds = []
        self.path_queue = []
        self.visited = [None] * maze.height
        for i in range(0,maze.height):
            self.visited[i] = [None] * maze.length
            for j in range(0, maze.length):
                self.visited[i][j] = [False] * maze.width

    def __get_path(self, node):
        if node.parent != None:
            self.__get_path(node.parent)
        self.path_queue.append(node)


    def get_path(self):
        self.__get_path(Search.found)
        return self.path_queue


    def BFS(self):
        self.ds.append(self.start_node)
        self.visited[self.start_node.i][self.start_node.j][self.start_node.k] = True
        while self.ds and Search.found == None:
            s = self.ds.pop(0)
            children = s.get_children_nodes()
            for child in children:
                if self.visited[child.i][child.j][child.k] == False:
                    self.ds.append(child)
                    self.visited[child.i][child.j][child.k] = True
        print("BFS cost is " + str(Search.found.get_path()))


    def UCSheap(self):
        self.ds.append((0,self.start_node))
        self.visited[self.start_node.i][self.start_node.j][self.start_node.k] = True
        while self.ds and Search.found == None:
            
            s= heapq.heappop(self.ds)
            if s[1].n == 'E':
                print("found")
                break
            print("looking")
            print(s[0])
            children = s[1].get_children_nodes()
            for child in children:
                print(child)
                if self.visited[child.i][child.j][child.k] == False:
                    self.visited[child.i][child.j][child.k] = True
                    if s[1].n == "A" or s[1].n == 'S' or s[1].n == 'E':
                        heapq.heappush(self.ds,(s[0] + 1, child))
                        #self.ds.append((s[0] + 1, child))
                    else:
                        heapq.heappush(self.ds,(s[0] + s[1].n, child)) 
                        #self.ds.append((s[0] + s[1].n, child))
                    print(self.ds)

        print("UCS cost is " + str(Search.found.get_path()))


    def UCS(self):
        list = PriorityQueue()
        list.put((100000,self.start_node))
        list.put((0, self.start_node))

        while not list.empty():
            s = list.get()
            if s[1].n == 'E':
                print("found")
                break
            print("looking")
            children = s[1].get_children_nodes()
            for child in children:
                print(child)
                list.put((child.n, child))
                print(list)


    def DFS(self):
        Node.queue = []
        self.ds.append(self.start_node)
        while self.ds and Search.found == None:
            s = self.ds.pop()
            if self.visited[s.i][s.j][s.k] == False:
                    self.visited[s.i][s.j][s.k] = True
                    children = s.get_children_nodes()
                    for child in children:
                         if self.visited[child.i][child.j][child.k] == False:
                            self.ds.append(child)
        print("DFS cost is " + str(Search.found.get_path()))

                   