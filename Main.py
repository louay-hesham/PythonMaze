from Core import *
from GUI import *

x = MainGUI()
x.on_execute()
maze = x.maze
n = maze.start_node

print ("printing")
print (n.get_children_nodes())
print ("done")