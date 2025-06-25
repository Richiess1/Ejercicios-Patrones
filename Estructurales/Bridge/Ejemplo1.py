# Implementor
class Color:
    def apply_color(self):
        pass

# Concrete Implementors
class Red(Color):
    def apply_color(self):
        return "red"

class Blue(Color):
    def apply_color(self):
        return "blue"

# Abstraction
class Shape:
    def __init__(self, color: Color):
        self.color = color

    def draw(self):
        pass

# Refined Abstractions
class Circle(Shape):
    def draw(self):
        print(f"Drawing a circle in {self.color.apply_color()}")

class Square(Shape):
    def draw(self):
        print(f"Drawing a square in {self.color.apply_color()}")
        
# Crear colores
red = Red()
blue = Blue()

# Combinar formas con colores (puente)
circle_red = Circle(red)
circle_red.draw()   # Output: Drawing a circle in red

square_blue = Square(blue)
square_blue.draw()  # Output: Drawing a square in blue

square_red = Square(red)
square_red.draw()   # Output: Drawing a square in red 