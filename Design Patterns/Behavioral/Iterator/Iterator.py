from abc import ABC, abstractmethod
class Iterator(ABC):
    @abstractmethod
    def has_next(self):
        pass

    @abstractmethod
    def next(self):
        pass

class MovieIterator(Iterator):
    def __init__(self, movie_list):
        self.movie_list = movie_list
        self.index = 0

    def has_next(self):
        return self.index < self.movie_list.get_size()

    def next(self):
        movie = self.movie_list.get_movie(self.index)
        self.index += 1
        return movie

