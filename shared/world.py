import copy

from shared.geometry import WorldPoint
from shared.nibble import Nibble


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

    def get_empty_positions(self, distance=None):
        if distance is None:
            distance = 0
        empty_positions = []
        for iy in range(self.get_height()):
            for ix in range(self.get_width()):
                p = WorldPoint(self, ix, iy)
                distance_empty = True
                if self.is_empty(p):
                    for idy in range(distance):
                        for idx in range(distance):
                            dp = WorldPoint(self, ix + idx - distance/2,  iy + idy - distance/2)
                            if not self.is_empty(dp):
                                distance_empty = False
                    if distance_empty:
                        empty_positions.append(p)
        return empty_positions

    def get_view_of_nibble(self, nibble):
        pos = nibble.get_position()
        if self.get(pos) is not nibble:
            raise "Nibble is not on this world or out of sync (positions do not match)!"
        view = ''
        for iy in range(5):
            for ix in range(5):
                p = WorldPoint(self, pos.get_x() + ix - 2, pos.get_y() + iy - 2)
                value = self.get(p)
                if isinstance(value, Nibble):
                    if nibble.get_energy() > value.get_energy():
                        view += '>'
                    elif nibble.get_energy() < value.get_energy():
                        view += '<'
                    else:
                        view += '='
                else:
                    view += str(value)
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
                value = self._world.get(WorldPoint(self._world, x, y))
                if isinstance(value, Nibble):
                    line += value.get_name()
                else:
                    line += value
            print line
