import arcade

class Game(arcade.Window):                          #arcade.Window is a class in arcade library
    def __init__(self):
        super().__init__(width=950 , height=600 , title= "interestellar game 2024")
        arcade.set_background_color(arcade.color.BLACK_OLIVE)
        self.background = arcade.load_texture(":resources:images/backgrounds/stars.png")
        self.me = spaceship(self)

    def on_draw(self):                              #This meyhod i for showing something
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, self.width, self.height, self.background)
        self.me.draw()



    
class spaceship(arcade.Sprite):
    def __init__(self  , game):             #game in sapceship = self in game
        super().__init__(":resources:images/space_shooter/playerShip1_orange.png")
        self.center_x = game.width//2
        self.center_y = 50




class enemy:
    ...





window = Game()

arcade.run()