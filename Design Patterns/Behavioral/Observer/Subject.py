from abc import ABC, abstractmethod
class SubjectInterface(ABC):
    @abstractmethod
    def subscribe(self, subscriber):
        pass

    @abstractmethod
    def unsubscribe(self, subscriber):
        pass

    @abstractmethod
    def notify_subscribers(self, video_title):
        pass

class YoutubeChannel(SubjectInterface):
    def __init__(self, name):
        self.name = name
        self.subscribers = []

    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)

    def unsubscribe(self, subscriber):
        try:
            self.subscribers.remove(subscriber)
        except ValueError as e:
            print(f"Error while removing subscriber: {e}")

    def notify_subscribers(self, video_title):
        for subscriber in self.subscribers:
            subscriber.update(self.name, video_title)

    def upload_video(self, video_title):
        print(f'Uploaded video {video_title}')
        self.notify_subscribers(video_title)
