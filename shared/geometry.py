class Point(object):
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def set_x(self, x):
        self._x = x

    def set_y(self, y):
        self._y = y

    def move(self, dx, dy):
        self._x += dx
        self._y += dy

    def __str__(self):
        return "Point({0}, {1})".format(self._x, self._y)

class WorldPoint(Point):
    def __init__(self, world, x=0, y=0):
        self._world = world
        self._x = 0
        self._y = 0
        self.set_x(x)
        self.set_y(y)

    def set_x(self, x):
        self._x = self._clip_x(self._x, x)

    def set_y(self, y):
        self._y = self._clip_y(self._y, y)

    def _clip_x(self, x, dx):
        return (x + dx) % self._world.get_width()

    def _clip_y(self, y, dy):
        return (y + dy) % self._world.get_height()

    def move(self, dx, dy):
        self._x = self._clip_x(self._x, dx)
        self._y = self._clip_y(self._y, dy)

    def __eq__(self, obj):
        if isinstance(obj, WorldPoint):
            return obj.get_x() == self.get_x() and obj.get_y() == self.get_y()
        return False
