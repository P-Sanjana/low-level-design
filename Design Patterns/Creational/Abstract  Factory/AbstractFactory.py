from abc import ABC, abstractmethod
import AbstractProduct
class GUIFactory(ABC):
    @abstractmethod
    def create_button(self):
        pass

    @abstractmethod
    def create_checkbox(self):
        pass

class WindowsFactory(GUIFactory):
    def create_button(self):
        return AbstractProduct.WindowsButton()

    def create_checkbox(self):
        return AbstractProduct.WindowsCheckbox()

class MacOSFactory(GUIFactory):
    def create_button(self):
        return AbstractProduct.MacOSButton()

    def create_checkbox(self):
        return AbstractProduct.MacOSCheckbox()
