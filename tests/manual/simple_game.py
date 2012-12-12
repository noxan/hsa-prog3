from shared.nibble import Nibble
from shared.world import World, WorldStringRenderer


world = World(10, 10)
wrender = WorldStringRenderer(world)

a = Nibble('a', world)
b = Nibble('b', world)
c = Nibble('c', world)

wrender.render()
print a, b, c

a.move(-1,1)
b.move_code(18)
c.move(-1,-2)

wrender.render()
print a, b, c
