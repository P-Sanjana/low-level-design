from FileSystemItem import FileSystemItem
class File(FileSystemItem):
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def get_size(self):
        return self.size

    def print_structure(self, indent):
        print(f"{indent} - {self.name} ({self.size} KB")

    def delete_item(self):
        print(f"Deleting file: {self.name}")

class Folder(FileSystemItem):
    def __init__(self, name):
        self.name = name
        self.children = []

    def add_item(self, item):
        self.children.append(item)

    def get_size(self):
        total = 0
        for item in self.children:
            total += item.get_size()
        return total

    def print_structure(self, indent):
        print(f"{indent} + {self.name}/")
        for item in self.children:
            item.print_structure(indent + ' ')


    def delete_item(self):
        for item in self.children:
            item.delete_item()
        print(f'Deleting folder: {self.name}')
