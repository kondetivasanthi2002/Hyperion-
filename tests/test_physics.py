"""Automated Test Suite 3: Physics Engine Tests"""
import unittest
from engine.core.vector import Vector2D
from engine.physics.rigidbody import Rigidbody2D
from engine.physics.physics_world import PhysicsWorld

class TestPhysicsEngine(unittest.TestCase):
    def test_rigidbody_integration(self):
        body = Rigidbody2D(mass=2.0)
        body.apply_force(Vector2D(10.0, 0.0))
        body.integrate(1.0, gravity=Vector2D.zero())
        self.assertTrue(body.velocity.x > 0.0)

    def test_physics_world_step(self):
        world = PhysicsWorld(gravity=Vector2D(0.0, -9.81))
        body = Rigidbody2D(mass=1.0)
        body.position = Vector2D(0.0, 10.0)
        world.add_body(body)
        world.step(0.1)
        self.assertTrue(body.position.y < 10.0)

if __name__ == '__main__':
    unittest.main()
