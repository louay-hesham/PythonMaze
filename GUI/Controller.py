class Controller(object):
    
    def __init__(self, maze, nodes): #Controller constructor
        self.step = 0
        self.nodes = nodes
        self.maze = maze
        self.maze.step_start = (nodes[0].i, nodes[0].j, nodes[0].k)
        self.maze.step_end = (nodes[1].i, nodes[1].j, nodes[1].k)
 
    def next_step(self): 
        if self.step < (len(self.nodes) - 2):
            self.step += 1
            self.maze.step_start = (self.nodes[self.step].i, self.nodes[self.step].j, self.nodes[self.step].k)
            self.maze.step_end = (self.nodes[self.step + 1].i, self.nodes[self.step + 1].j, self.nodes[self.step + 1].k)
 
    def prev_step(self):
        if self.step > 0:
            self.step -= 1
            self.maze.step_start = (self.nodes[self.step].i, self.nodes[self.step].j, self.nodes[self.step].k)
            self.maze.step_end = (self.nodes[self.step + 1].i, self.nodes[self.step + 1].j, self.nodes[self.step + 1].k)
 
   


