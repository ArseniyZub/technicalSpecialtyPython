class Rectangle:
    def __init__(self, length, width=None):
        if width is None:
            self.length = self.width = length
        else:
            self.length = length
            self.width = width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def area(self):
        return self.length * self.width

rectangle = Rectangle(5, 3) 
print("Периметр:", rectangle.perimeter())
print("Площадь:", rectangle.area())         