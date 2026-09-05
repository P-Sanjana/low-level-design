from abc import ABC, abstractmethod
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass

class InsertCommand(Command):
    def __init__(self, document, text):
        self.document = document
        self.text = text

    def execute(self):
        self.document.insert(self.text)

    def undo(self):
        self.document.delete(len(self.text))

class DeleteCommand(Command):
    def __init__(self, document, char_length):
        self.document = document
        self.prev_text = ''
        self.char_length = char_length

    def execute(self):
        self.prev_text = self.document.get_last_text(self.char_length)
        self.document.delete(self.char_length)

    def undo(self):
        self.document.insert(self.prev_text)
        self.prev_text = ''
