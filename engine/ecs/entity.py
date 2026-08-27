"""
ECS Architecture - Entity Manager
Manages entity creation, destruction, generational indices, and component composition bitmasks.
"""

from typing import Set, Dict, Type, Optional
from engine.ecs.component import BaseComponent, ComponentRegistry

class Entity:
    """Represents a lightweight integer handle in the ECS world."""
    __slots__ = ('id', 'generation', 'active')

    def __init__(self, entity_id: int, generation: int = 0):
        self.id = entity_id
        self.generation = generation
        self.active = True

    def __hash__(self) -> int:
        return hash((self.id, self.generation))

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Entity):
            return False
        return self.id == other.id and self.generation == other.generation

    def __repr__(self) -> str:
        return f"Entity(id={self.id}, gen={self.generation})"
