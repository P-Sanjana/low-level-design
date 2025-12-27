import platform
import AbstractFactory

class Application:
    def __init__(self, factory):
        self.button = factory.create_button()
        self.checkbox = factory.create_checkbox()

    def render_ui(self):
        self.button.paint()
        self.checkbox.paint()

class AppLauncher:
    @staticmethod
    def main():
        os = platform.system()
        if 'Windows' in os:
            factory = AbstractFactory.WindowsFactory()
        else:
            factory = AbstractFactory.MacOSFactory()
        app = Application(factory)
        app.render_ui()

if __name__ == '__main__':
    AppLauncher.main()