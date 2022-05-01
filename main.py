from ui import UserInterface
from session import Session
from player import Player

player = Player()
ui = UserInterface(player)
session = Session(ui, player)

ui.mainloop()
