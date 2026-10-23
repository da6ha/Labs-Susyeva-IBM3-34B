from .point import Point

class Segment(Point):
    def __init__(self, x1, y1, color1, x2, y2, color2, seg_color):
        Point.__init__(self, x1, y1, seg_color)
        self.x1, self.y1, self.color1 = x1, y1, color1
        self.x2, self.y2, self.color2 = x2, y2, color2

    def length(self):
        dx = self.x2 - self.x1
        dy = self.y2 - self.y1
        return (dx * dx + dy * dy) ** 0.5

    def area(self):
        return 0

    def move(self, dx, dy):
        super().move(dx, dy)
        self.x1 += dx
        self.y1 += dy
        self.x2 += dx
        self.y2 += dy

    def display(self):
        print("Отрезок:")
        print(f"  Начало: ({self.x1:.2f}, {self.y1:.2f}), Цвет: {self.color1}")
        print(f"  Конец: ({self.x2:.2f}, {self.y2:.2f}), Цвет: {self.color2}")
        print(f"  Длина = {self.length():.2f}")
        print(f"  Цвет отрезка = {self.color}")