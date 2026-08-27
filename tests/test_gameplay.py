"""Automated Test Suite 5: Gameplay Mechanics & Stats Tests"""
import unittest
from engine.gameplay.stats import StatBlock
from engine.gameplay.inventory import InventoryBag, Item

class TestGameplayMechanics(unittest.TestCase):
    def test_stat_block_leveling(self):
        stats = StatBlock(health=100.0, mana=50.0)
        leveled = stats.add_exp(120)
        self.assertTrue(leveled)
        self.assertEqual(stats.level, 2)

    def test_inventory_capacity_and_adding(self):
        bag = InventoryBag(capacity=2)
        i1 = Item("sword", "Iron Sword", "Weapon")
        i2 = Item("potion", "Health Potion", "Consumable")
        i3 = Item("shield", "Wooden Shield", "Armor")
        
        self.assertTrue(bag.add_item(i1))
        self.assertTrue(bag.add_item(i2))
        self.assertFalse(bag.add_item(i3))

if __name__ == '__main__':
    unittest.main()
