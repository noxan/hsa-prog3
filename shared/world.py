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

    def is_empty(self, x, y):
        return self.get(x, y) == '.'

    def get(self, x, y):
        return self._world[x][y]

    def set(self, x, y, obj):
        if not self.is_empty(x, y):
            raise "Field is not empty"
        self._world[x][y] = obj

    def move(self, x, y, obj, tx, ty):
        if tx != x and ty != y:
            self.set(tx, ty, obj)
            self.set(x, y, '.')

    def get_width(self):
        return self._width

    def get_height(self):
        return self._height

class WorldStringRenderer(object):
    def __init__(self, world):
        self._world = world

    def render(self):
        for x in range(self._world.get_width()):
            line = ''
            for y in range(self._world.get_height()):
                line += self._world.get(x, y)
            print line
