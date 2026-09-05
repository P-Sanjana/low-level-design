from Document import Document
from Command import InsertCommand, DeleteCommand
class TextEditor:
    def __init__(self, document):
        self.document = document
        self.undo_stack, self.redo_stack = [], []

    def execute_command(self, command):
        command.execute()
        self.undo_stack.append(command)
        self.redo_stack.clear()

    def undo(self):
        if not self.undo_stack:
            return
        command = self.undo_stack.pop()
        command.undo()
        self.redo_stack.append(command)

    def redo(self):
        if not self.redo_stack:
            return
        command = self.redo_stack.pop()
        command.execute()
        self.undo_stack.append(command)

    def show(self):
        print("Text: ", self.document)


if __name__ == '__main__':
    document = Document()
    insert_command = InsertCommand(document, "hello world")
    delete_command = DeleteCommand(document, 5)
    text_editor = TextEditor(document)

    text_editor.execute_command(insert_command)
    text_editor.show()
    text_editor.execute_command(delete_command)

    text_editor.show()

    text_editor.undo()
    text_editor.show()

    text_editor.redo()
    text_editor.show()
