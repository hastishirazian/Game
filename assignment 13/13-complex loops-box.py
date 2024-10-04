import arcade

class Pattern(arcade.Window):

    def __init__(self):
        super().__init__(width=500 , height=500 , title= "Complex loops-box")
        arcade.set_background_color(arcade.color.ALMOND)
        self.row = 10
        self.column = 10
        self.form_object = Form(self.design)


    def on_draw(self):
        arcade.start_render()
        self.form_object.draw()


class Form(arcade.Sprite):

    def __init__(self, Pattern):
        for row in range (10):
            for column in range(10):

                if column%2 == 0:
                    print("🔴")

                elif column%2 == 1:
                    print("🔵")


object1 = Pattern()    
arcade.run()