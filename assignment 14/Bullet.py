import arcade

class bullet(arcade.Sprite): 
    def __init__(self, host):
        super().__init__(":resources:images/space_shooter/laserRed01.png")
        self.center_x = host.center_x
        self.center_y = host.center_y
        self.speed = 4

    def move(self):
        self.center_y += self.speed
