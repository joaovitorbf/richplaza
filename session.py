import requests
import urllib
from PIL import ImageTk, Image
from io import BytesIO
from threading import Timer, main_thread, Thread
from time import sleep, time


class Session:
    def __init__(self, ui, player):
        self.req = requests.session()
        self.ui = ui
        self.length = 1
        self.initialtime = time()
        self.lastupdate = 0
        self.player = player
        self.playercheck = False

        Thread(target=self.update_interface, daemon=True).run()
        Thread(target=self.update_listeners, daemon=True).run()

    def get_status(self):
        r = self.req.get("https://api.plaza.one/status")
        res = r.json()
        return res

    def update_interface(self):
        print("update_interface")
        if not main_thread().is_alive():
            return
        if (time() - self.lastupdate) < 2:
            Timer(3, self.update_interface)
            return

        self.lastupdate = time()
        if not self.playercheck: self.check_player()

        try:
            info = self.get_status()
        except requests.exceptions.ConnectionError:
            print("update_interface connection error, retrying")
            timer = Timer(5, self.update_interface)
            timer.daemon = True
            timer.start()
            return

        print(info)
        self.ui.set_track_name(info['song']['title'])
        self.ui.set_artist_name(info['song']['artist'])
        self.ui.set_reactions(info['song']['reactions'])

        img = ImageTk.PhotoImage(Image.open(BytesIO(self.req.get(
            info['song']['artwork_sm_src']).content)).resize((109, 109)))
        self.ui.set_album_cover(img)

        self.length = info['song']['length']
        self.position = info['song']['position']
        self.initialtime = int(time())-info['song']['position']

        if self.ui.is_playing():
            print("update")
            self.ui.presence.update(state="by {}".format(info['song']['artist']),
                                    details=info['song']['title'],
                                    end=self.initialtime+self.length,
                                    large_image='nightwave')

        self.update_time()

    def update_time(self):
        print("update_time")
        if not main_thread().is_alive():
            return

        if not self.playercheck: self.check_player()

        self.ui.set_time(self.length, int(time()) -
                         self.initialtime, self.initialtime+self.length)

        if int(time())-self.initialtime < self.length:
            timer = Timer(0.5, self.update_time)
            timer.daemon = True
            timer.start()
        else:
            self.update_interface()

    def update_listeners(self):
        print("update_listeners")
        if not main_thread().is_alive():
            return

        if not self.playercheck: self.check_player()

        try:
            r = self.req.get("https://api.plaza.one/status/on-screen-data")
        except requests.exceptions.ConnectionError:
            print("update_listeners connection error, retrying")
            timer = Timer(5, self.update_listeners)
            timer.daemon = True
            timer.start()
            return
        self.ui.set_listeners(r.json()[1])
        timer = Timer(10, self.update_listeners)
        timer.daemon = True
        timer.start()

    def check_player(self):
        self.playercheck = False
        if self.ui.shouldbeplaying and not self.player.is_playing():
            self.playercheck = True
            print("check_player connection error, retrying")
            self.player.configure()
            self.player.play()
            timer = Timer(3, self.check_player)
            timer.daemon = True
            timer.start()