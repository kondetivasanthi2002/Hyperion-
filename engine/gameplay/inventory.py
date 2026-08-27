"""
Gameplay Engine - Inventory & Item System
Implements Item, ItemRarity, InventoryBag, EquipmentManager, and item serialization.
"""

from typing import List, Dict, Optional

class Item:
    """Represents an inventory item."""
    def __init__(self, item_id: str, name: str, item_type: str, rarity: str = "Common", value: int = 10, stackable: bool = False, max_stack: int = 99):
        self.item_id = item_id
        self.name = name
        self.item_type = item_type
        self.rarity = rarity
        self.value = value
        self.stackable = stackable
        self.max_stack = max_stack
        self.quantity = 1


class InventoryBag:
    """Manages player item storage, capacity limits, and stacking."""

    def __init__(self, capacity: int = 20):
        self.capacity = capacity
        self.items: List[Item] = []

    def add_item(self, item: Item) -> bool:
        if item.stackable:
            for existing in self.items:
                if existing.item_id == item.item_id and existing.quantity < existing.max_stack:
                    space = existing.max_stack - existing.quantity
                    add_qty = min(space, item.quantity)
                    existing.quantity += add_qty
                    item.quantity -= add_qty
                    if item.quantity <= 0:
                        return True
        if len(self.items) < self.capacity:
            self.items.append(item)
            return True
        return False
