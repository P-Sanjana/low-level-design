from abc import ABC, abstractmethod
class Button(ABC):
    @abstractmethod
    def paint(self):
        pass

    @abstractmethod
    def on_click(self):
        pass

class Checkbox(ABC):
    @abstractmethod
    def paint(self):
        pass

    @abstractmethod
    def on_click(self):
        pass

class WindowsButton(Button):
    def paint(self):
        print(f"Painting windows button")

    def on_click(self):
        print(f"Clicking windows button")

class MacOSButton(Button):
    def paint(self):
        print(f"Painting Mac OS button")

    def on_click(self):
        print(f"Clicking Mac OS button")

class WindowsCheckbox(Checkbox):
    def paint(self):
        print(f"Painting windows checkbox")

    def on_click(self):
        print(f"Clicking windows checkbox")

class MacOSCheckbox(Checkbox):
    def paint(self):
        print(f"Painting Mac OS checkbox")

    def on_click(self):
        print(f"Clicking Mac OS checkbox")
