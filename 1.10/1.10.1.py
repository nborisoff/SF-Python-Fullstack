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

print(r1.get_info())