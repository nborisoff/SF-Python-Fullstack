class Rectangle:
    def __init__(self, l, w):
        self.length = l
        self.width = w

    def rectangle_area(self):
        return self.length * self.width

    def rectangle_info(self):
        return 'Длина прямоугольника: %s, ширина прямоугольника: %s\nПлощадь прямоугольника: %s' % (self.length, self.width, self.rectangle_area())

newRectangle = Rectangle(12, 10)

print(newRectangle.rectangle_info())