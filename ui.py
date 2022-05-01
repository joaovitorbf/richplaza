from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter
from tkinter.font import Font
from math import floor
import datetime
import pypresence

class UserInterface:
    def __init__(self, player) -> None:
        # Init Tk
        self.root = Tk()
        self.root.title("Rich Plaza")
        self.root.geometry("470x180")
        self.root.iconbitmap("favicon.ico")
        self.root.resizable(False, False)
        self.playing = player.is_playing()
        self.end = 0
        self.player = player

        self.presence = pypresence.Presence("970102086194827294")
        self.presence.connect()

        WCELLS = 24
        HCELLS = 3

        def nothing(): messagebox.showinfo(title="Oops!", message="This button is still a WIP!")

        # Style definitions
        style = ttk.Style(self.root)
        style.theme_use("classic")
        style.configure("ToolBar.TButton", highlightthickness=-5)
        style.map("ToolBar.TButton", relief=[("pressed", SUNKEN), ("!active", FLAT), ("active", RAISED)])
        style.configure("TButton", highlightthickness=-5)

        # Main window frame
        mainframe = ttk.Frame(self.root, padding=2)
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        # Toolbar buttons
        about_btn = ttk.Button(mainframe, text="About", padding="3 2 3 2", style="ToolBar.TButton", command=nothing)
        about_btn.grid(column=1, row=1, sticky="ew")
        #history_btn = ttk.Button(mainframe, text="Play History", padding="3 2 3 2", style="ToolBar.TButton", command=nothing)
        #history_btn.grid(column=2, row=1, sticky="ew")
        #ratings_btn = ttk.Button(mainframe, text="Ratings", padding="3 2 3 2", style="ToolBar.TButton", command=nothing)
        #ratings_btn.grid(column=3, row=1, sticky="ew")
        #donate_btn = ttk.Button(mainframe, text="Donate", padding="3 2 3 2", style="ToolBar.TButton", command=nothing)
        #donate_btn.grid(column=4, row=1, sticky="ew")
        #account_btn = ttk.Button(mainframe, text="Sign In", padding="3 2 3 2", style="ToolBar.TButton", command=nothing)
        #account_btn.grid(column=WCELLS, row=1, sticky="nsew")

        # Central player frame
        player_frame = ttk.Frame(mainframe, padding=10, width=466, height=130, border=1, relief=SUNKEN)
        player_frame.grid_propagate(False)
        player_frame.grid(column=1, row=2, columnspan=WCELLS, sticky="ew")

        # Bottom text frame
        listeners_frame = ttk.Frame(mainframe, padding=0, width=466, height=20, border=1, relief=SUNKEN)
        listeners_frame.grid_propagate(False)
        listeners_frame.grid(column=1, row=HCELLS, columnspan=WCELLS, sticky="sew")

        # Album cover
        cover_frame = ttk.Frame(player_frame, padding=0, width=110, height=110, border=1, relief=SUNKEN)
        cover_frame.grid_propagate(False)
        cover_frame.grid(column=1, row=1)
        self.cover_label = ttk.Label(cover_frame, borderwidth=0)
        self.cover_label.grid(row = 0, column = 0)

        # Details and controls frame
        detandcont_frame = ttk.Frame(player_frame, padding="5 0 0 0", width=335, height=110, border=0, relief=SUNKEN)
        detandcont_frame.grid_propagate(False)
        detandcont_frame.grid(column=2, row=1, sticky="we")

        self.artist_text = StringVar()
        self.artist_text.set("Test Name")
        self.artist_label = ttk.Label(detandcont_frame, textvariable=self.artist_text, font=('Verdana', '11', 'bold'))
        self.artist_label.grid(column=1, row=1, columnspan=2 , sticky="w")

        self.track_text = StringVar()
        self.track_text.set("Test Track")
        self.track_label = ttk.Label(detandcont_frame, textvariable=self.track_text, font=('Verdana', '11'))
        self.track_label.grid(column=1, row=2, columnspan=2, sticky="w")

        time_frame = ttk.Frame(detandcont_frame, padding=0, width=170, height=25, border=1, relief=SUNKEN)
        time_frame.grid_propagate(False)
        time_frame.grid(column=1, row=3)
        detandcont_frame.rowconfigure(3, pad=15)

        self.time_text = StringVar()
        self.time_text.set("00:00 / 00:00")
        self.time_label = ttk.Label(time_frame, textvariable=self.time_text, font=('Verdana', '10'), justify='center')
        self.time_label.place(x=85, y=11, anchor="center")

        def setvolume(val): player.audio_set_volume(int(round(float(val))))
        volume_scale = ttk.Scale(detandcont_frame, orient=HORIZONTAL, length=130, from_=0, to=100, command=setvolume, value=100)
        volume_scale.grid(column=2, row=3)
        detandcont_frame.columnconfigure(2, pad=15)

        self.volume_image = PhotoImage(file="volume.png")
        volume_img_label = ttk.Label(detandcont_frame, image=self.volume_image)
        volume_img_label.grid(column=3, row=3)

        # Frame for the three control buttons
        ctrlbtns_frame = ttk.Frame(detandcont_frame, padding="0 0 0 0", height=26, border=0, relief=SUNKEN)
        ctrlbtns_frame.grid_propagate(False)
        ctrlbtns_frame.grid(column=1, row=4, sticky="we", columnspan=4)
        ctrlbtns_frame.columnconfigure(1,minsize=170)
        ctrlbtns_frame.columnconfigure(2,minsize=41)
        ctrlbtns_frame.columnconfigure(3,minsize=111)

        def play():
            self.playing = player.is_playing()
            if self.playing:
                self.presence.clear()
                self.playbtn_text.set("Play")
                player.stop()
            else:
                self.playbtn_text.set("Stop")
                self.presence.update(state="by {}".format(self.artist_text.get()),
                    details=self.track_text.get(),
                    end=self.end,
                    large_image='nightwave')
                player.play()

        self.playbtn_text = StringVar()
        self.playbtn_text.set("Play")
        play_btn = ttk.Button(ctrlbtns_frame, textvariable=self.playbtn_text, padding="3 2 3 2", command=play)
        play_btn.grid(column=1, row=1, sticky="we")

        self.like_btn_text = StringVar()
        self.like_btn_text.set("♥ 0")
        like_btn = ttk.Button(ctrlbtns_frame, textvariable=self.like_btn_text, padding="3 2 3 2", width=4, command=nothing)
        like_btn.grid(column=2, row=1, sticky="we", padx=6)

        settings_btn = ttk.Button(ctrlbtns_frame, text="Settings", padding="3 2 3 2", command=nothing)
        settings_btn.grid(column=3, row=1, sticky="we")

    def mainloop(self):
        self.root.mainloop()

    def set_track_name(self, name):
        self.track_text.set(name)
    def set_artist_name(self, name):
        self.artist_text.set(name)
    def set_album_cover(self, img):
        self.cover_label.configure(image=img)
        self.cover_label.image = img
    def set_time(self, length, position, end):
        self.end = end
        timelen = str(datetime.timedelta(seconds=length)).split(':')
        timepos = str(datetime.timedelta(seconds=position)).split(':')
        self.time_text.set("{}:{} / {}:{}".format(timepos[1], timepos[2], timelen[1], timelen[2]))
    def set_reactions(self, reactions):
        self.like_btn_text.set("♥ {}".format(reactions))
    def is_playing(self):
        self.playing = self.player.is_playing()
        return self.playing