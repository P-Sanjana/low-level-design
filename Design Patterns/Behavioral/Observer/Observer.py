from abc import ABC, abstractmethod
class ObserverInterface(ABC):
    @abstractmethod
    def update(self, channel, video_title):
        pass

class User(ObserverInterface):
    def __init__(self, name):
        self.name = name

    def update(self, channel, video_title):
        print(f'{self.name} got notified: {video_title} was uploaded on channel {channel}')

    
