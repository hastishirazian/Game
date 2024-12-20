import arcade

class spaceship(arcade.Sprite):
    def __init__(self , game):                                                  #game in sapceship = self in game
        super().__init__(":resources:images/space_shooter/playerShip1_orange.png")
        self.center_x = game.width//2
        self.center_y = 50
        self.speed = 10

    def move(self,direction):
        if direction == "L":
            self.center_x = self.center_x - self.speed
        elif direction == "R":
            self.center_x = self.center_x + self.speed