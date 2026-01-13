from Subsystems import TV, SoundSystem, DVDPlayer
class RemoteControlFacade:
    def __init__(self):
        self.tv = TV()
        self.soundSystem = SoundSystem()
        self.dvdPlayer = DVDPlayer()

    def watchMovie(self):
        self.tv.turnOn()
        self.tv.setHDMIPort(4432)
        self.soundSystem.turnOn()
        self.soundSystem.setVolume(30)
        self.dvdPlayer.turnOn()
        self.dvdPlayer.play()

    def powerOff(self):
        self.tv.turnOff()
        self.soundSystem.turnOff()
        self.dvdPlayer.turnOff()

