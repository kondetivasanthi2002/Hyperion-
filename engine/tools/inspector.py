"""
Tools Engine - Entity Scene Inspector & Property Grid
Provides live scene hierarchy inspection, component property grid editor, and debug hooks.
"""

from typing import Dict, Any, List
from engine.ecs.entity import Entity

class EntityInspector:
    """Inspects active ECS entities and formats property grid data."""
    def __init__(self):
        self.selected_entity: Entity = None

    def inspect_entity(self, entity: Entity, components: Dict[str, Any]) -> Dict[str, Any]:
        self.selected_entity = entity
        return {
            "entity_id": entity.id,
            "components": {k: str(v) for k, v in components.items()}
        }
