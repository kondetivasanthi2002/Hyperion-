"""
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
