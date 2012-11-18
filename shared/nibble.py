from shared.geometry import Point

class Nibble(object):
    _energy = 0
    _position = Point(0, 0)

    def __init__(self, position=Point(0,0), energy=30):
        self._energy = energy
        self._position = position

    def get_position(self):
        return self._position

    def get_position_x(self):
        return self._position._x

    def get_position_y(self):
        return self._position._y

    def get_energy(self):
        return self._energy
