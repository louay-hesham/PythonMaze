from abc import ABC, abstractmethod

class Search(ABC):
    @abstractmethod
    def get_solution(self, maze):
        pass


