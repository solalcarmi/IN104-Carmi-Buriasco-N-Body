import unittest
from ..utils.vector import Vector2
from .. import World, Body
from ..simulator import Simulator

class CollisionneurTestCase(unittest.TestCase):

    def test_collisions(self):
        b1 = Body(Vector2(0, 0),velocity=Vector2(0.1, 0),mass=100,draw_radius=5)
        b2 = Body(Vector2(0, 0),velocity=Vector2(0.05, 0),mass=50,draw_radius=5, color=(0, 255, 0))
        
        
        world = World()
        world.add(b1)
        world.add(b2)

        id2 = self.world.add(b2)
        
        
        
        check_for_collisions(world)
        
        
        
        self.assertIsNone(id2)
        
        
        
        m = self.world.get(id1).mass
        self.assertEqual(m, 150)
        
        
        v = self.world.get(id2).velocity
        self.assertEqual(v[0] == 0.15)
        self.assertEqual(v[1] == 0)