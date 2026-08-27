import os
import subprocess

def run_cmd(cmd, cwd="."):
    res = subprocess.run(cmd, shell=True, capture_output=True, text=True, cwd=cwd)
    return res.stdout, res.stderr, res.returncode

def write_file(filepath, content):
    dirname = os.path.dirname(filepath)
    if dirname:
        os.makedirs(dirname, exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")

print("Generating Entity-Component-System (engine/ecs/)...")

# component.py
component_code = '''"""
ECS Architecture - Component Definitions
Defines component base class, bitmask component types, and standard engine components.
"""

from typing import Dict, Type, Any
from engine.core.vector import Vector2D, Vector3D

class BaseComponent:
    """Base class for all data components in the ECS framework."""
    __slots__ = ()

class TransformComponent(BaseComponent):
    """Component holding spatial position, rotation, and scale."""
    __slots__ = ('position', 'rotation', 'scale')

    def __init__(self, position: Vector3D = None, rotation: Vector3D = None, scale: Vector3D = None):
        self.position = position if position else Vector3D.zero()
        self.rotation = rotation if rotation else Vector3D.zero()
        self.scale = scale if scale else Vector3D.one()

class VelocityComponent(BaseComponent):
    """Component holding linear and angular velocities."""
    __slots__ = ('linear', 'angular')

    def __init__(self, linear: Vector3D = None, angular: Vector3D = None):
        self.linear = linear if linear else Vector3D.zero()
        self.angular = angular if angular else Vector3D.zero()

class RenderComponent(BaseComponent):
    """Component storing visual mesh, sprite texture, color tint, and layer."""
    __slots__ = ('sprite_id', 'color_rgba', 'visible', 'z_index')

    def __init__(self, sprite_id: str = "default", color_rgba: Tuple[float, float, float, float] = (1.0, 1.0, 1.0, 1.0), visible: bool = True, z_index: int = 0):
        self.sprite_id = sprite_id
        self.color_rgba = color_rgba
        self.visible = visible
        self.z_index = z_index

class HealthComponent(BaseComponent):
    """Component managing entity hitpoints and armor state."""
    __slots__ = ('current_hp', 'max_hp', 'shield', 'invulnerable')

    def __init__(self, max_hp: float = 100.0, shield: float = 0.0):
        self.max_hp = float(max_hp)
        self.current_hp = float(max_hp)
        self.shield = float(shield)
        self.invulnerable = False

    def is_alive(self) -> bool:
        return self.current_hp > 0.0

    def take_damage(self, amount: float) -> float:
        if self.invulnerable or amount <= 0:
            return 0.0
        remaining_dmg = amount
        if self.shield > 0:
            absorbed = min(self.shield, remaining_dmg)
            self.shield -= absorbed
            remaining_dmg -= absorbed
        self.current_hp = max(0.0, self.current_hp - remaining_dmg)
        return amount

    def heal(self, amount: float):
        if amount > 0:
            self.current_hp = min(self.max_hp, self.current_hp + amount)

class ComponentRegistry:
    """Assigns unique bitmask flags to component classes for O(1) query matching."""
    _type_to_bit: Dict[Type[BaseComponent], int] = {}
    _next_bit = 0

    @classmethod
    def get_bit(cls, component_type: Type[BaseComponent]) -> int:
        if component_type not in cls._type_to_bit:
            cls._type_to_bit[component_type] = 1 << cls._next_bit
            cls._next_bit += 1
        return cls._type_to_bit[component_type]
'''

write_file("engine/ecs/component.py", component_code)

# entity.py
entity_code = '''"""
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
'''

write_file("engine/ecs/entity.py", entity_code)

# world.py
world_code = '''"""
ECS Architecture - World Manager
Central manager for entity lifecycles, component storage tables, system ticks, and query caches.
"""

from typing import Dict, List, Set, Type, Optional, Tuple
from engine.ecs.entity import Entity
from engine.ecs.component import BaseComponent, ComponentRegistry

class World:
    """Main ECS World managing entity storage and system pipelines."""

    def __init__(self):
        self._next_entity_id = 1
        self._entities: Dict[int, Entity] = {}
        self._components: Dict[Type[BaseComponent], Dict[int, BaseComponent]] = {}
        self._entity_bitmasks: Dict[int, int] = {}
        self._systems: List[Any] = []

    def create_entity(self) -> Entity:
        eid = self._next_entity_id
        self._next_entity_id += 1
        entity = Entity(eid)
        self._entities[eid] = entity
        self._entity_bitmasks[eid] = 0
        return entity

    def destroy_entity(self, entity: Entity):
        if entity.id in self._entities:
            eid = entity.id
            for comp_type in list(self._components.keys()):
                if eid in self._components[comp_type]:
                    del self._components[comp_type][eid]
            del self._entity_bitmasks[eid]
            del self._entities[eid]

    def add_component(self, entity: Entity, component: BaseComponent):
        comp_type = type(component)
        if comp_type not in self._components:
            self._components[comp_type] = {}
        self._components[comp_type][entity.id] = component
        bit = ComponentRegistry.get_bit(comp_type)
        self._entity_bitmasks[entity.id] |= bit

    def get_component(self, entity: Entity, component_type: Type[BaseComponent]) -> Optional[BaseComponent]:
        if component_type in self._components:
            return self._components[component_type].get(entity.id)
        return None

    def query(self, required_types: List[Type[BaseComponent]]) -> List[Tuple[Entity, ...]]:
        if not required_types:
            return []
        mask = 0
        for comp_type in required_types:
            mask |= ComponentRegistry.get_bit(comp_type)
        
        results = []
        for eid, bitmask in self._entity_bitmasks.items():
            if (bitmask & mask) == mask:
                ent = self._entities[eid]
                comps = tuple(self._components[ct][eid] for ct in required_types)
                results.append((ent,) + comps)
        return results

    def add_system(self, system: Any):
        self._systems.append(system)

    def update(self, dt: float):
        for system in self._systems:
            if hasattr(system, 'update'):
                system.update(self, dt)
'''

write_file("engine/ecs/world.py", world_code)

# Commit Git
run_cmd("git add .")
run_cmd('git commit -m "feat(ecs): implement high-performance Entity-Component-System framework"')
print("Commit 3 completed.")
