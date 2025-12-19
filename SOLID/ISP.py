# violates Interface Segregation principle
from abc import ABC, abstractmethod
class MediaPlayer:
    @abstractmethod
    def play_audio(self, audio_file):
        pass
    @abstractmethod
    def play_video(self, video_file):
        pass
    @abstractmethod
    def stop_audio(self):
        pass
    @abstractmethod
    def stop_video(self):
        pass
    @abstractmethod
    def adjust_audio_volume(self, volume):
        pass
    @abstractmethod
    def adjust_video_brightness(self, brightness):
        pass

# satisfies ISP
class AudioPlayer:
    @abstractmethod
    def play_audio(self, audio_file):
        pass

    @abstractmethod
    def stop_audio(self):
        pass

    @abstractmethod
    def adjust_audio_volume(self, volume):
        pass

class VideoPlayer:
    @abstractmethod
    def play_video(self, video_file):
        pass

    @abstractmethod
    def stop_video(self):
        pass

    @abstractmethod
    def adjust_video_brightness(self, brightness):
        pass

class MP3Player(AudioPlayer):
    def play_audio(self, audio_file):
        print("Playing audio")

    def stop_audio(self):
        print("Audio stopped")

    def adjust_audio_volume(self, volume):
        print("Adjusted audio volume")

class MP4VideoPlayer(VideoPlayer):
    def play_video(self, video_file):
        print("Playing video")

    def stop_video(self):
        print("Video stopped")

    def adjust_video_brightness(self, brightness):
        print("Adjusted video brightness")