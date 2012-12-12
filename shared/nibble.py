from shared.geometry import Point
from shared.utils import movement_to_energy, code_to_movement


class Nibble(object):
    def __init__(self, name, world, position=None, energy=30):
        self._name = name
        self._world = world
        if position:
            self._position = position
        else:
            self._position = Point(0, 0)
        self._energy = energy

    def move_code(self, code):
        code = int(code)
        movement = code_to_movement(code)
        return self.move_vector(movement[0], movement[1])

    def move(self, delta_x, delta_y):
        delta_energy = movement_to_energy(delta_x, delta_y)
        self._energy -= delta_energy
        self._position._x += delta_x
        self._position._y += delta_y

    def get_name(self):
        return self._name

    def get_position(self):
        return self._position

    def get_position_x(self):
        return self._position._x

    def get_position_y(self):
        return self._position._y

    def get_energy(self):
        return self._energy
