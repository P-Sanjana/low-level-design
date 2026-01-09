from TextDecorator import TextDecorator
class BoldDecorator(TextDecorator):
    def __init__(self, inner):
        super().__init__(inner)

    def render(self):
        print('<b>', end='')
        self.inner.render()
        print('</b>', end='')

class ItalicDecorator(TextDecorator):
    def __init__(self, inner):
        super().__init__(inner)

    def render(self):
        print('<i>', end='')
        self.inner.render()
        print('</i>', end='')

class UnderlineDecorator(TextDecorator):
    def __init__(self, inner):
        super().__init__(inner)

    def render(self):
        print('<u>', end='')
        self.inner.render()
        print('</u>', end='')
