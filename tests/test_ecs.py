"""Automated Test Suite 2: ECS Architecture Tests"""
import unittest
from engine.ecs.world import World
from engine.ecs.component import TransformComponent, HealthComponent

class TestECSFramework(unittest.TestCase):
    def test_entity_creation_and_destruction(self):
        world = World()
        e1 = world.create_entity()
        e2 = world.create_entity()
        self.assertNotEqual(e1.id, e2.id)

    def test_component_binding_and_query(self):
        world = World()
        e = world.create_entity()
        health = HealthComponent(max_hp=150.0)
        world.add_component(e, health)
        
        fetched = world.get_component(e, HealthComponent)
        self.assertIsNotNone(fetched)
        self.assertEqual(fetched.max_hp, 150.0)

if __name__ == '__main__':
    unittest.main()
