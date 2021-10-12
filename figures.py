class Rectangle():
    def __init__(self, width=0, height=0):
        assert(width >= 0)
        assert(height >= 0)
        self.width = width
        self.height = height

    def set_width(self, width):
        assert(width >= 0)
        self.width = width 

    def set_height(self, height):
        assert(height >= 0)
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)


class Square(Rectangle):
    def set_width(self, width):
        assert(width >= 0)
        self.width = width
        self.height = width

    def set_height(self, height):
        assert(height >= 0)
        self.width = height
        self.height = height