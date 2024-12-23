import arcade
import random

class enemy(arcade.Sprite):
    def __init__(self , w , h):
        super().__init__(":resources:images/space_shooter/playerShip1_blue.png")
        self.center_x = random.randint(0,w)
        self.center_y = h + 24
        self.angle = 180
        self.speed = 3

    def move(self):
        self.center_y -= self.speed


class bullet(arcade.Sprite):
    def __init__(self ,host):
        super.__init__(":resources:images/space_shooter/laserRed01.png")
        self.center_x = host.center_x
        self.center_y = host.center_y
        self.speed = 4
        self.change_x = 0
        self.change_y = 1

    def move(self):
        self.center_y += self.speed