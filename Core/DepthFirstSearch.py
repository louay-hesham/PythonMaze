from Core import *

from Core.Search import Search
from Core.Node import Node
class DepthFirstSearch(Search):

    def __init__(self, start_node):
        return super().__init__(start_node)
        
    def get_children(self, node):
        x=set('3')
        x = Node.get_children_nodes(node)
        return x



    def get_solution(self,maze):
        visited = []
        stack = [maze.start_node]
        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.append(vertex)
                print("visit")
                print(list(visited))               
                print("hena")
                
                stack.append(vertex.get_children_nodes() - set(visited))

        print(visited)
        return visited

    def dfs(self, maze, start, end):
        stack = set()
        stack.add(start)
        visited = set()
        while stack:
            vertex = stack.pop()
            visited.add(vertex)
            for n in self.get_children:
                if n not in visited:
                    stack.push(n)
        return visited  
    

    def dfs_paths(self,graph, start, end):
        print("here")
        stack = [(start, [start])]
        print("stack")
        print(stack)
        while stack:
            (vertex, path) = stack.pop()
            print(path)
            for next in graph[vertex] - set(path):
                if next == end:
                    yield path + [next]
                else:
                    stack.append((next, path + [next]))