from abc import ABC, abstractmethod

class Search(ABC, object):

    def __init__(self, start_node):
        self.start_node = start_node
        self.ds = [start_node]

    @abstractmethod
    def get_solution(self, maze):
        pass


