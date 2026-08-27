"""
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
