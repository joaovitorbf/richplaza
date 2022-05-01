import vlc


class Player:
    def __init__(self) -> None:
        self.volume = 100
        self.configure()

    def configure(self):
        try:
            self.player.stop()
            self.vlcinstance.release()
            self.player.release()
        except:
            self.vlcinstance = vlc.Instance()
        self.player = self.vlcinstance.media_player_new()
        self.media = self.vlcinstance.media_new("http://radio.plaza.one/mp3")
        self.player.set_media(self.media)
        self.player.audio_set_volume(self.volume)

    def play(self):
        self.player.play()

    def stop(self):
        self.player.stop()

    def is_playing(self):
        return self.player.is_playing()

    def audio_set_volume(self, vol):
        self.volume = vol
        self.player.audio_set_volume(vol)
