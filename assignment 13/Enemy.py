class enemy(arcade.Sprite):
    def __init__(self , w , h):
        super().__init__(":resources:images/space_shooter/playerShip1_blue.png")
        self.center_x = random.randint(0,w)
        self.center_y = h + 24
        self.angle = 180
        self.speed = 3

    def move(self):
        self.center_y -= self.speed