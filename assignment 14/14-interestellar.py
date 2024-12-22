import arcade
import random
from Spaceship import spaceship
from Enemy import enemy 

class Game(arcade.Window):                                                      #arcade.Window is a class in arcade library
    
    def __init__(self):
        super().__init__(width=950 , height=600 , title= "interestellar game 2024")
        arcade.set_background_color(arcade.color.CATALINA_BLUE)
        self.background = arcade.load_texture(":resources:images/backgrounds/stars.png")
        self.me = spaceship(self)                   # object of spaceship
        self.enemys = []

    def on_draw(self):                                                          #This meyhod i for showing something
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, self.width, self.height, self.background)
        self.me.draw()
        for i in self.enemys:
            i.draw()
        arcade.finish_render()

    def on_key_press(self , symbol: int ,modifiers: int):
        
        if symbol == arcade.key.LEFT or symbol == arcade.key.A:      
            self.me.change_x = -1
        elif symbol == arcade.key.RIGHT or symbol == arcade.key.D:    
            self.me.change_x = 1       
        elif symbol == arcade.key.SPACE:
            ...

    def on_update(self , delta_time: float):
        for i in self.enemys:
            i.move()
        if random.randint(1 , 100) == 5:
            self.new_enemy = enemy(self.width, self.height)
            self.enemys.append(self.new_enemy)







window = Game()
arcade.run()