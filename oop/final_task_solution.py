"""Sample solution for the shape area take-home task."""


class Shape:
    def describe(self):
        return "This is a shape."


class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def describe(self):
        area = self.width * self.height
        return "Rectangle: %.2f x %.2f, area %.2f" % (
            self.width,
            self.height,
            area,
        )


class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def describe(self):
        area = 3.14 * self.radius * self.radius
        return "Circle: radius %.2f, area %.2f" % (self.radius, area)


if __name__ == "__main__":
    shapes = [Rectangle(4, 5), Circle(3)]
    for shape in shapes:
        print(shape.describe())