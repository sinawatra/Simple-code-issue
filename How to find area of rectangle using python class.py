#3. 3. Write a Python class named Rectangle constructed from length and width and a method that will compute the area of a rectangle.
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
rectangle = Rectangle(12, 23)
print('Area of rectangle:', rectangle.area())