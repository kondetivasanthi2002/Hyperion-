"""
Gameplay Engine - Save State Serialization Manager
Handles JSON state encoding, checkpoint loading, and player progression persistence.
"""

import json
from typing import Dict, Any

class SaveState:
    """Manages player progression save data and inventory state serialization."""

    @staticmethod
    def serialize_player(level: int, exp: int, hp: float, coins: int, inventory: list) -> str:
        data = {
            "version": "1.0.0",
            "player": {
                "level": level,
                "exp": exp,
                "hp": hp,
                "coins": coins
            },
            "inventory": [item.get("name") if isinstance(item, dict) else str(item) for item in inventory]
        }
        return json.dumps(data, indent=2)

    @staticmethod
    def deserialize_player(json_str: str) -> Dict[str, Any]:
        return json.loads(json_str)
