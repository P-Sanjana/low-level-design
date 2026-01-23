from abc import ABC, abstractmethod
class AbstractTreeType(ABC):
    def __init__(self, name, texture, color):
        self.name = name
        self.texture = texture
        self.color = color

    @abstractmethod
    def draw(self, x, y):
        pass

class TreeType(AbstractTreeType):
    def __init__(self, name, texture, color):
        super().__init__(name, texture, color)

    def draw(self, x, y):
        print(f'Drawing {self.name} tree at {x}, {y} position with {self.texture} and {self.color}')

    