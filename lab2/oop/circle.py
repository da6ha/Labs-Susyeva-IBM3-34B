from .point import Point

class Circle(Point):
    def __init__(self, cx, cy, center_color, radius, circle_color):
        Point.__init__(self, cx, cy, circle_color)
        self.cx, self.cy = cx, cy
        self.center_color = center_color
        self.radius = radius

    def length(self):
        return 2 * 3.14 * self.radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def move(self, dx, dy):
        super().move(dx, dy)
        self.cx += dx
        self.cy += dy

    def display(self):
        print("Окружность:")
        print(f"  Центр: ({self.cx:.2f}, {self.cy:.2f}), Цвет: {self.center_color}")
        print(f"  Радиус = {self.radius:.2f}")
        print(f"  Длина = {self.length():.2f}")
        print(f"  Площадь = {self.area():.2f}")
        print(f"  Цвет окружности = {self.color}")