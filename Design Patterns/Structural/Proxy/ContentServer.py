from abc import ABC, abstractmethod
class ContentServer(ABC):
    def fetchData(self, url):
        pass