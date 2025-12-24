class Singleton:
    _instance = None

    def __init__(self):
        if Singleton._instance is not None:
            raise Exception('Use get_instance() method')

    @staticmethod
    def get_instance():
        if Singleton._instance == None:
            Singleton._instance = Singleton()
        return Singleton._instance

print(Singleton.get_instance().__class__)
