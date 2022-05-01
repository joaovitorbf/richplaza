from ui import UserInterface
from session import Session
from player import Player
from presence import Presence

if __name__ == "__main__":
    presence = Presence()
    player = Player()
    ui = UserInterface(player, presence)
    session = Session(ui, player, presence)

    ui.mainloop()
