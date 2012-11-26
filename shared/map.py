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

    def get(self, x, y):
        return self._map[x][y]

    def get_width(self):
        return self._width

    def get_height(self):
        return self._height
