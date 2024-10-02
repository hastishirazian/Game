import arcade

class Pattern(arcade.Window):

    def __init__(self):
        super().__init__(width=500 , height=500 , title= "Complex loops-box")
        arcade.set_background_color(arcade.color.ALMOND)
        self.line = 10

    def on_draw(self):
        arcade.start_render()

        for line in range (10):
            




object1 = Pattern()    

arcade.run()