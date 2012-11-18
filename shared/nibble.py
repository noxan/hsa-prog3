from shared.geometry import Point

class Nibble(object):
    _energy = 0
    _position = Point(0, 0)

    def __init__(self, position=Point(0,0), energy=30):
        self._energy = energy
        self._position = position
