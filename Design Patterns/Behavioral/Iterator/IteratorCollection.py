from abc import ABC, abstractmethod
from Iterator import MovieIterator
class IteratorCollection(ABC):
    @abstractmethod
    def create_iterator(self):
        pass

class MovieCollection(IteratorCollection):
    def __init__(self):
        self.movie_list = []

    def add_movie(self, movie):
        self.movie_list.append(movie)

    def get_size(self):
        return len(self.movie_list)

    def get_movie(self, index):
        if index < 0 or index >= self.get_size():
            print('Invalid index')
        return self.movie_list[index]

    def create_iterator(self):
        return MovieIterator(self)
