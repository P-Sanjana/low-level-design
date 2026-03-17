from Subject import YoutubeChannel
from Observer import User
def youtube_demo():
    youtube_channel = YoutubeChannel("Design Patterns")

    alice = User("Alice")
    bob = User("Bob")

    youtube_channel.subscribe(alice)
    youtube_channel.subscribe(bob)

    youtube_channel.upload_video("Observer Design Pattern")

    youtube_channel.unsubscribe(bob)

    youtube_channel.upload_video("Behavioral Patterns Recap")


if __name__ == '__main__':
    youtube_demo()
