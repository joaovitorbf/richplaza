from ui import UserInterface
import vlc

vlcinstance = vlc.Instance()
player=vlcinstance.media_player_new()
media=vlcinstance.media_new("http://radio.plaza.one/mp3")
player.set_media(media)

ui = UserInterface(player)
ui.mainloop()