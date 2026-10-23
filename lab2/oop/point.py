from abc import ABC, abstractmethod

class Point(ABC):
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    @abstractmethod
    def length(self):
        pass

    @abstractmethod
    def area(self):
        pass

    def display(self):
        print("Точка:")
        print(f"  X = {self.x:.2f}, Y = {self.y:.2f}, Цвет = {self.color}")