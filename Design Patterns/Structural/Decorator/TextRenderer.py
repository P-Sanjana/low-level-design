from Decorators import BoldDecorator, ItalicDecorator, UnderlineDecorator
from PlainTextView import PlainTextView
class TextRenderer:
    @staticmethod
    def main():
        text = PlainTextView("Hello World!")
        print("Plain: ", end='')
        text.render()
        print()

        bold_text = BoldDecorator(text)
        print('Bold: ', end='')
        bold_text.render()
        print()

        italic_text = ItalicDecorator(text)
        print('Italic: ', end='')
        italic_text.render()
        print()

        underline_text = BoldDecorator(UnderlineDecorator(text))
        print('Bold + Underline: ', end='')
        underline_text.render()
        print()

        all_types = UnderlineDecorator(ItalicDecorator(BoldDecorator(text)))
        print('All types: ', end='')
        all_types.render()

if __name__ == '__main__':
    TextRenderer.main()
