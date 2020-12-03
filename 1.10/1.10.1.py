class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = height
        self.height = width

    def get_info(self):
        #return 'Rectangle (%s, %s, %s, %s)' % (self.x, self.y, self.width, self.height)
        return 'Rectangle (' + str(self.x) + ', ' + str(self.y) + ', ' + str(self.width) + ', ' + str(self.height) + ')'


r1 = Rectangle(5, 10, 50, 100)
r2 = Rectangle(10, 20, 100, 150)

print(r1.get_info())
print(r2.get_info())