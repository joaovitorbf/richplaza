import pypresence
from tkinter import messagebox
from multiprocessing import Process, Queue
from time import sleep


class Presence:
    def __init__(self) -> None:
        self.q = Queue()
        Process(target=self.process, daemon=True, args=(self.q,)).start()

    def process(self, q):
        self.configure()
        while True:
            item = q.get()
            if item != 'clear':
                self.apply_update(item[0], item[1], item[2])
            else:
                self.presence.clear()
            sleep(1)

    def configure(self):
        print("start presence")
        self.presence = pypresence.Presence("970102086194827294")
        self.presence.connect()
        print("presence connected")

    def apply_update(self, artist, track, end):
        self.presence.update(state="by {}".format(artist),
                             details=track,
                             end=end,
                             large_image='nightwave')

    def update(self, artist, track, end):
        self.q.put((artist, track, end))

    def clear(self):
        self.q.put('clear')
