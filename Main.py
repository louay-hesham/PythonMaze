from Core import *
from GUI import *

x = MainGUI()
x.on_execute()
maze = x.maze
n = Node(0,3,3,maze)

print ("printing")
print (n.get_children_nodes())
print ("done")