class Controller(object):
    
    def __init__(self, nodes):
        self.step = 0
        self.nodes = nodes
 
    def next_step(self):
        self.step += 1
 
    def prev_step(self):
        self.step -= 1
 
   


