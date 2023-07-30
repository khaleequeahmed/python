class Remote():
    pass
# Encapsulation -->Player ke code player main
class Player:
    def moveup(self):
        pass
    def movedown(self):
        pass
    def moveright(self):
        pass
    def moveleft(self):
        pass

remote1 = Remote()
player1 = Player()

if (remote1.isleftpressed()):
    player1.moveleft()

