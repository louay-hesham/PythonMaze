from Core import *
from GUI import *

x = MainGUI()
x.on_execute()
maze = x.maze
s = maze.start_node
search = Search(s, maze)
search.DFS()
search.BFS()
