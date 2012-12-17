from shared.nibble import Nibble
from shared.world import NibbleWorld, WorldStringRenderer


world = NibbleWorld(10, 10)
wrender = WorldStringRenderer(world)

a = Nibble('a', world)
a.move(-1,1)
b = Nibble('b', world)
b.move_code(18)
c = Nibble('c', world)
c.move(-1,-2)


wrender.render()
print a, b, c

print world.get_view_of_nibble(a)

world.spawn_food(5)
wrender.render()
