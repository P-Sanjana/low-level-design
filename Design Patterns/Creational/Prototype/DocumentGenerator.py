from DocumentRegistry import DocumentRegistry
from DocumentPrototype import Document
class DocumentGenerator:
    @staticmethod
    def main():
        registry = DocumentRegistry()
        registry.register('Invoice', Document('Invoice', 'Nvidia', 'GPU', 'OpenAI', 10000, 200))
        registry.register('Contract', Document('Contract', 'Microsoft', 'Storage', 'GitHub', 20000, 10))

        document1 = registry.get('Invoice')
        print(document1)

        document2 = registry.get('Invoice')
        document2.set_customer_name('Meta')
        print(document2)

        document3 = registry.get('Contract')
        print(document3)

if __name__ == '__main__':
    DocumentGenerator.main()

