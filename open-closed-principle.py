# Open-Closed principle states that software entities like object, class and modules should be open for extension and closed 
# for modification

# For exmaple - Shape is abstract class which will be then extended by other classes and implement the methods present in the
# abstract class

# Violates open closed principle
class ShapeDrawer:
    def draw(self, shape_type):
        if shape_type == "rectangle":
            print("Drawing rectangle")
        elif shape_type == "circle":
            print("Drawing circle")

shape = ShapeDrawer()
shape.draw("rectangle")
shape.draw("circle")

# Valid Example

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass

class Rectangle(Shape):
    def draw(self):
        print("drawing rectangle")

class Circle(Shape):
    def draw(self):
        print("drawing circle")

class ShapeDrawer:
    def draw(self, shape:Shape):
        shape.draw()

drawer = ShapeDrawer()

circle = Circle()
rectangle = Rectangle()

drawer.draw(circle)
drawer.draw(rectangle)


        