from oop import Segment, Circle

COLORS = ["красный", "оранжевый", "жёлтый", "зелёный", "голубой", "синий", "фиолетовый", "розовый", "белый", "чёрный", "серый"]

def input_number(a):
    while True:
        try:
            return float(input(a))
        except ValueError:
            print("  Это не число. Попробуйте ещё раз.")

def input_color(a):
    while True:
        text = input(a).strip().lower()
        if text == "-": return "розовый"
        if text in COLORS: return text
        print("  Такого цвета нет.")

print("Доступные цвета:", ", ".join(COLORS), "\n")

print("Введите первую точку:")
x1, y1 = input_number("  X: "), input_number("  Y: ")
color1 = input_color("  Цвет: ")

print("Введите вторую точку:")
x2, y2 = input_number("  X: "), input_number("  Y: ")
color2 = input_color("  Цвет: ")

segment_color = input_color("Введите цвет отрезка: ")
segment = Segment(x1, y1, color1, x2, y2, color2, segment_color)

print("Введите центр окружности:")
cx, cy = input_number("  X: "), input_number("  Y: ")
center_color = input_color("  Цвет центра: ")
radius = input_number("Введите радиус: ")
circle_color = input_color("Введите цвет окружности: ")

circle = Circle(cx, cy, center_color, radius, circle_color)

print("\n" + "=" * 50)
segment.display()
print()
circle.display()

print("\nПеремещение фигур")
dx = input_number("На сколько сдвинуть по X: ")
dy = input_number("На сколько сдвинуть по Y: ")

segment.move(dx, dy)
circle.move(dx, dy)

print(f"\nПеремещаем на ({dx:.2f}, {dy:.2f})\n")
segment.display()
print()
circle.display()
print("=" * 50)