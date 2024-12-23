import arcade
from Bullet import bullet

class spaceship(arcade.Sprite):
    def __init__(self , w , game):          
        super().__init__(":resources:images/space_shooter/playerShip1_orange.png")
        self.center_x = game.width//2
        self.center_y = 50
        self.change_x = 0
        self.change_y = 0
        self.speed = 5
        self.game_width = w
        self.bullet_list = []    


    def move(self):
        if self.change_x == -1:
            if self.center_x > 0:
                self.center_x -= self.speed

        elif self.change_x == 1:
            if self.center_x < self.game_width:
                self.center_x += self.speed

    def fire(self):
        new_bullet = bullet(self)
        self.bullet_list.append(new_bullet)