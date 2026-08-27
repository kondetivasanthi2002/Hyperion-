"""
Gameplay Engine - RPG Stats & Character Attributes
Implements StatBlock, Attributes, StatModifiers, EXP Leveling Curves, and Skill Tree definitions.
"""

from typing import Dict, List

class StatModifier:
    """Stat modifier representing flat or percentage stat boosts."""
    def __init__(self, stat_name: str, value: float, is_percent: bool = False):
        self.stat_name = stat_name
        self.value = float(value)
        self.is_percent = is_percent

class StatBlock:
    """Character RPG stat block handling health, mana, attributes, and modifier recalculations."""

    def __init__(self, health: float = 100.0, mana: float = 50.0, strength: int = 10, agility: int = 10, intelligence: int = 10):
        self.base_max_hp = health
        self.current_hp = health
        self.base_max_mp = mana
        self.current_mp = mana
        self.strength = strength
        self.agility = agility
        self.intelligence = intelligence
        
        self.level = 1
        self.exp = 0
        self.exp_to_next_level = 100
        self.modifiers: List[StatModifier] = []

    def add_exp(self, amount: int) -> bool:
        self.exp += amount
        leveled_up = False
        while self.exp >= self.exp_to_next_level:
            self.exp -= self.exp_to_next_level
            self.level += 1
            self.exp_to_next_level = int(self.exp_to_next_level * 1.5)
            self.base_max_hp += 20
            self.base_max_mp += 10
            self.strength += 2
            self.agility += 2
            self.intelligence += 2
            self.current_hp = self.get_max_hp()
            self.current_mp = self.get_max_mp()
            leveled_up = True
        return leveled_up

    def get_max_hp(self) -> float:
        hp = self.base_max_hp + self.strength * 5
        for mod in self.modifiers:
            if mod.stat_name == "max_hp":
                hp += (hp * mod.value) if mod.is_percent else mod.value
        return hp

    def get_max_mp(self) -> float:
        mp = self.base_max_mp + self.intelligence * 5
        for mod in self.modifiers:
            if mod.stat_name == "max_mp":
                mp += (mp * mod.value) if mod.is_percent else mod.value
        return mp
