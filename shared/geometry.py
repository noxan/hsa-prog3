class Point(object):
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def move(self, dx, dy):
        self._x += dx
        self._y += dy

    def __str__(self):
        return "Point({0}, {1})".format(self._x, self._y)

class WorldPoint(Point):
    def __init__(self, world, x=0, y=0):
        self._world = world
        return super(WorldPoint, self).__init__(x, y)
