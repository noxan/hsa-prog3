from shared.nibble import Nibble
from shared.world import World, WorldStringRenderer


world = World(10, 10)
wrender = WorldStringRenderer(world)

wrender.render()
print "-------------------------"

n = Nibble('a', world)
print n


wrender.render()
print n

n.move_code(18)

wrender.render()
print n
