import arcade
import random
from Spaceship import spaceship
from Enemy import enemy 
from Bullet import bullet

class Game(arcade.Window):                                       #arcade.Window is a class in arcade library
    
    def __init__(self):
        super().__init__(width=950 , height=600 , title= "interestellar game 2024")
        arcade.set_background_color(arcade.color.CATALINA_BLUE)
        self.background = arcade.load_texture(":resources:images/backgrounds/stars.png")
        self.me = spaceship(self.width, self)                    # object of spaceship
        self.enemys = []
        self.enemy_speed = 3 
        arcade.schedule(self.add_enemy, 3)

    def add_enemy(self, delta_time):

        new_enemy = enemy(self.width, self.height)
        self.enemys.append(new_enemy)
        self.enemy_speed += 0.2

        print(f"{self.enemy_speed}")  

    def on_draw(self):                                           #This meyhod i for showing something
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, self.width, self.height, self.background)
        self.me.draw()

        for i in self.enemys:
            i.draw()

        for i in self.me.bullet_list:
            i.draw()

        arcade.finish_render()


    def on_key_press(self , symbol: int ,modifiers: int):
        
        if symbol == arcade.key.LEFT or symbol == arcade.key.A:      
            self.me.change_x = -1
        elif symbol == arcade.key.RIGHT or symbol == arcade.key.D:    
            self.me.change_x = 1       
        elif symbol == arcade.key.SPACE:  
            self.me.fire()


    def on_key_release(self, symbol: int, modifiers: int):
        if symbol in [arcade.key.LEFT, arcade.key.RIGHT, arcade.key.A, arcade.key.D]:
            self.me.change_x = 0


    def on_update(self , delta_time: float):

        self.me.move()

        for i in self.enemys:
            i.move()

        if random.randint(1 , 100) == 5:
            self.new_enemy = enemy(self.width, self.height)
            self.enemys.append(self.new_enemy)

        for i in self.me.bullet_list:
            i.move()

        for i in self.enemys:
            if arcade.check_for_collision(self.me , i):
                print("^^^^^^^^^^^^^^^^^^^^^^Game over💀^^^^^^^^^^^^^^^^^^^^^^")
                exit(0)

        for i in self.enemys:
            for j in self.me.bullet_list:
                if arcade.check_for_collision(i, j):
                    self.enemys.remove(i)
                    self.me.bullet_list.remove(j)

        for i in self.enemys:
            if i.center_y < 0 :
                self.enemys.remove(i)



window = Game()
arcade.run()  