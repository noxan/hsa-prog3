import copy

from shared.geometry import WorldPoint


class World(object):
    def __init__(self, width, height):
        self._width = width
        self._height = height
        self.clear()

    def clear(self):
        self._world = []
        for x in range(self._width):
            self._world.append([])
            for y in range(self._height):
                self._world[x].append('.')

    def is_empty(self, point):
        return self.get(point) == '.'

    def get(self, point):
        return self._world[point.get_x()][point.get_y()]

    def set(self, point, obj):
        #if not self.is_empty(x, y):
        self._world[point.get_x()][point.get_y()] = obj

    def set_empty(self, point):
        self.set(point, '.')

    def move(self, point, obj, dx, dy):
        tpoint = copy.deepcopy(point)
        tpoint.move(dx, dy)
        if point != tpoint:
            self.set(tpoint, obj)
            self.set_empty(point)

    def get_width(self):
        return self._width

    def get_height(self):
        return self._height

class WorldStringRenderer(object):
    def __init__(self, world):
        self._world = world

    def render(self):
        for y in range(self._world.get_height()):
            line = ''
            for x in range(self._world.get_width()):
                line += self._world.get(WorldPoint(self._world, x, y))
            print line
