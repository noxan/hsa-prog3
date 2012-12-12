class Map(object):
    def __init__(self, width, height):
        self._width = width
        self._height = height
        self.clear()

    def clear(self):
        self._map = []
        for x in range(self._width):
            self._map.append([])
            for y in range(self._height):
                self._map[x].append('.')

    def is_empty(self, x, y):
        return self.get(x, y) == '.'

    def get(self, x, y):
        return self._map[x][y]

    def set(self, x, y, obj):
        if not self.is_empty(x, y):
            raise "Field is not empty"
        self._map[x][y] = obj

    def get_width(self):
        return self._width

    def get_height(self):
        return self._height
