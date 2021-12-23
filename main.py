from tkinter import *
from tkinter import ttk
from tkinter.font import Font

root = Tk()
root.title("Rich Plaza")
root.geometry("470x180")
root.resizable(False, False)

WCELLS = 24
HCELLS = 3

style = ttk.Style(root)
style.theme_use("classic")
style.configure("ToolBar.TButton", highlightthickness=-5)
style.map("ToolBar.TButton", relief=[("pressed", SUNKEN), ("!active", FLAT), ("active", RAISED)])

mainframe = ttk.Frame(root, padding=2)
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

about_btn = ttk.Button(mainframe, text="About", padding="3 2 3 2", style="ToolBar.TButton")
about_btn.grid(column=1, row=1, sticky="ew")
history_btn = ttk.Button(mainframe, text="Play History", padding="3 2 3 2", style="ToolBar.TButton")
history_btn.grid(column=2, row=1, sticky="ew")
ratings_btn = ttk.Button(mainframe, text="Ratings", padding="3 2 3 2", style="ToolBar.TButton")
ratings_btn.grid(column=3, row=1, sticky="ew")
donate_btn = ttk.Button(mainframe, text="Donate", padding="3 2 3 2", style="ToolBar.TButton")
donate_btn.grid(column=4, row=1, sticky="ew")

account_btn = ttk.Button(mainframe, text="Sign In", padding="3 2 3 2", style="ToolBar.TButton")
account_btn.grid(column=WCELLS, row=1, sticky="nsew")

player_frame = ttk.Frame(mainframe, padding=10, width=466, height=130, border=1, relief=SUNKEN)
player_frame.grid_propagate(False)
player_frame.grid(column=1, row=2, columnspan=WCELLS, sticky="ew")

listeners_frame = ttk.Frame(mainframe, padding=0, width=466, height=20, border=1, relief=SUNKEN)
listeners_frame.grid_propagate(False)
listeners_frame.grid(column=1, row=HCELLS, columnspan=WCELLS, sticky="sew")

cover_frame = ttk.Frame(player_frame, padding=0, width=110, height=110, border=1, relief=SUNKEN)
cover_frame.grid_propagate(False)
cover_frame.grid(column=1, row=1)

detandcont_frame = ttk.Frame(player_frame, padding="5 0 0 0", width=345, height=110, border=0, relief=SUNKEN)
detandcont_frame.grid_propagate(False)
detandcont_frame.grid(column=2, row=1)

artist_text = StringVar()
artist_text.set("Test Name")
artist_label = ttk.Label(detandcont_frame, textvariable=artist_text, font=('Verdana', '11', 'bold'))
artist_label.grid(column=1, row=1, columnspan=2 , sticky="w")

track_text = StringVar()
track_text.set("Test Track")
track_label = ttk.Label(detandcont_frame, textvariable=artist_text, font=('Verdana', '11'))
track_label.grid(column=1, row=2, columnspan=2, sticky="w")

time_frame = ttk.Frame(detandcont_frame, padding=0, width=170, height=25, border=1, relief=SUNKEN)
time_frame.grid_propagate(False)
time_frame.grid(column=1, row=3)
detandcont_frame.rowconfigure(3, pad=15)

volume_scale = ttk.Scale(detandcont_frame, orient=HORIZONTAL, length=130, from_=0, to=100)
volume_scale.grid(column=2, row=3)
detandcont_frame.columnconfigure(2, pad=15)


root.mainloop()