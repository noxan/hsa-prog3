class Point(object):
    _x = 0
    _y = 0

    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def move(self, delta_x, delta_y):
        self._x += delta_x
        self._y += delta_y

    def __str__(self):
        return "Point({0}, {1})".format(self._x, self._y)
