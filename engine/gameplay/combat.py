"""
Gameplay Engine - Combat Resolver & Status Effects
Implements DamageCalculators, Critical Hits, Status Effects (Poison, Burn, Stun), and Combat Logs.
"""

import random

class DamageCalculator:
    """Calculates physical, magical, and elemental damage mitigation."""

    @staticmethod
    def calculate_damage(attacker_str: float, weapon_atk: float, defender_armor: float) -> Tuple[float, bool]:
        base_dmg = attacker_str * 1.5 + weapon_atk
        armor_reduction = defender_armor / (defender_armor + 100.0)
        mitigated_dmg = base_dmg * (1.0 - armor_reduction)
        
        # 15% Critical hit chance
        is_crit = random.random() < 0.15
        if is_crit:
            mitigated_dmg *= 2.0
            
        return max(1.0, mitigated_dmg), is_crit
