import arcade

class Pattern(arcade.Window):

    def __init__(self):
        super().__init__(width=500, height=500, title="Complex loops-box")
        arcade.set_background_color(arcade.color.BRILLIANT_LAVENDER)

        self.diamond_size = 10  
        self.diamond_spacing = 30  
        self.form_object = Form(self) 

    def on_draw(self):
        arcade.start_render()
        self.form_object.draw()

class Form:
    def __init__(self, pattern):
        self.pattern = pattern
        self.row = 10
        self.column = 10

    def draw(self):
        for row in range(self.row):
            for column in range(self.column):
                x = 100 + column * self.pattern.diamond_spacing
                y = 100 + row * self.pattern.diamond_spacing

                color = arcade.color.BLUEBONNET if (row + column) % 2 == 0 else arcade.color.BRIGHT_PINK

                arcade.draw_circle_filled(center_x=x, center_y=y, radius=self.pattern.diamond_size, color=color)

window = Pattern()
arcade.run()