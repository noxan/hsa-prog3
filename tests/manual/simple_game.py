from shared.nibble import Nibble
from shared.world import World, WorldStringRenderer


world = World(10, 10)
wrender = WorldStringRenderer(world)

wrender.render()

n = Nibble('a', world)
print n
