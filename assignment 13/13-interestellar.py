import arcade
import random

class Game(arcade.Window):                          #arcade.Window is a class in arcade library
    def __init__(self):
        super().__init__(width=950 , height=600 , title= "interestellar game 2024")
        arcade.set_background_color(arcade.color.BLACK)
        self.background = arcade.load_texture(":resources:images/backgrounds/stars.png")
        self.me = spaceship(self)                   # object of spaceship
        self.enemy = enemy(self.width, self.height)

    def on_draw(self):                              #This meyhod i for showing something
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, self.width, self.height, self.background)
        self.me.draw()
        self.enemy.draw()

    def on_key_press(self , symbol: int ,modifiers: int):
        
        if symbol == 97:        # A
            self.me.center_x = self.me.center_x - self.me.speed
        elif symbol == 100:     # D
            self.me.center_x = self.me.center_x + self.me.speed

    def on_update(self , delta_time: float):
        self.enemy.center_y -= self.enemy.speed


    
class spaceship(arcade.Sprite):
    def __init__(self , game):                      #game in sapceship = self in game
        super().__init__(":resources:images/space_shooter/playerShip1_orange.png")
        self.center_x = game.width//2
        self.center_y = 50
        self.speed = 10


  

class enemy(arcade.Sprite):
    def __init__(self , w , h):
        super().__init__(":resources:images/space_shooter/playerShip1_blue.png")
        self.center_x = random.randint(0,w)
        self.center_y = h + 24
        self.angle = 180
        self.speed = 3




window = Game()

arcade.run()