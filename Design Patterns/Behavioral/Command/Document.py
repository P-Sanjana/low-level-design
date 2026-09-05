class Document:
    def __init__(self):
        self.text = ''

    def insert(self, t):
        self.text += t

    def delete(self, length):
        self.text = self.text[:-length]

    def get_last_text(self, length):
        return self.text[-length:]

    def __str__(self):
        return self.text
