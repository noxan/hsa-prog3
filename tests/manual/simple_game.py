from shared.nibble import Nibble
from shared.world import World, WorldStringRenderer


w = World(10, 10)
wrender = WorldStringRenderer(w)

wrender.render()

n = Nibble()
print n
