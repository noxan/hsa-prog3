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

    def get_view_of_nibble(self, nibble):
        pos = nibble.get_position()
        if self.get(pos) != nibble.get_name():
            raise "Nibble is not on this world or out of sync (positions do not match)!"
        view = ''
        for iy in range(5):
            py = pos.get_y() + iy - 2
            for ix in range(5):
                px = pos.get_x() + ix - 2
                p = WorldPoint(self, px, py)
                value = self.get(p)
                if value != '.' and value != '*':
                    value = '='
                view += value
            view += '\n'
        return view

    def move(self, point, dx, dy):
        tpoint = copy.deepcopy(point)
        tpoint.move(dx, dy)
        if point != tpoint:
            self.set(tpoint, self.get(point))
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
