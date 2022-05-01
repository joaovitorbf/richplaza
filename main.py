from ui import UserInterface
from session import Session
import vlc

vlcinstance = vlc.Instance()
player=vlcinstance.media_player_new()
media=vlcinstance.media_new("http://radio.plaza.one/mp3")
player.set_media(media)
player.audio_set_volume(100)

ui = UserInterface(player)
session = Session(ui)

ui.mainloop()