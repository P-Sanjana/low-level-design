from abc import ABC, abstractmethod
class FileSystemItem(ABC):
    @abstractmethod
    def get_size(self):
        pass

    @abstractmethod
    def print_structure(self, indent):
        pass

    @abstractmethod
    def delete_item(self):
        pass


