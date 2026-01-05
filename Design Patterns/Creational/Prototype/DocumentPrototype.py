from abc import ABC, abstractmethod
class DocumentPrototype(ABC):
    @abstractmethod
    def clone(self):
        pass

class Document(DocumentPrototype):
    def __init__(self, type, company_name, title, customer_name, price, quantity):
        self.type = type
        self.company_name = company_name
        self.title = title
        self.customer_name = customer_name
        self.price = price
        self.quantity = quantity

    def clone(self):
        # do shallow copy for mutable reference types
        return Document(self.type, self.company_name, self.title, self.customer_name, self.price, self.quantity)

    def set_customer_name(self, customer_name):
        self.customer_name = customer_name

    def __str__(self):
        return f'type={self.type}, company_name={self.company_name}, title={self.title}, customer_name={self.customer_name}, price={self.price}, quantity={self.quantity}'

