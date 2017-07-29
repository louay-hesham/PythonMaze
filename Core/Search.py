import heapq
from queue import PriorityQueue
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
            children = s.get_children_nodes()
            for child in children:
                if self.visited[child.i][child.j][child.k] == False:
                    self.ds.append(child)
                    self.visited[child.i][child.j][child.k] = True
        print("Cost is " + str(Search.found.get_path()))
      #  print(self.visited)

    def UCSheap(self):
        self.ds.append([0,self.start_node])
        self.visited[self.start_node.i][self.start_node.j][self.start_node.k] = True
        while self.ds and Search.found == None:
            heapq.heapify(self.ds)
            s= heapq.heappop(self.ds[0])
            print(s[0])
            if s[1].n == 'E':
                print("found")
                break
            print("looking")
            children = s[1].get_children_nodes()
            for child in children:
                #print(child)
                if self.visited[child.i][child.j][child.k] == False:
                    if child.n == "A":
                        self.ds.append([1,child])
                    else:
                        self.ds.append([child.n, child])
                    self.visited[child.i][child.j][child.k] = True
                    print(self.ds)

        print("Cost is ucs " + str(Search.found.get_path()))

    def DFS(self):
        self.ds.append(self.start_node)
        while self.ds and Search.found == None:
            s = self.ds.pop()
            if self.visited[s.i][s.j][s.k] == False:
                    self.visited[s.i][s.j][s.k] = True
                    children = s.get_children_nodes()
                    for child in children:
                         if self.visited[child.i][child.j][child.k] == False:
                            self.ds.append(child)

      #  print("hena")
     #   print(self.visited)
        print("Cost is dfs " + str(Search.found.get_path()))

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

        print("Cost is ucs " + str(Search.found.get_path()))


                   