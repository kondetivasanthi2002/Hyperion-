"""
Audio Engine - 3D Positional Audio Panning
Implements stereo spatial panning and distance attenuation for sound emitters.
"""

import math
from engine.core.vector import Vector2D

class SpatialAudioListener:
    """Audio listener representing player position in 2D/3D audio space."""
    def __init__(self, position: Vector2D = None):
        self.position = position if position else Vector2D.zero()

    def calculate_pan_and_gain(self, emitter_pos: Vector2D, max_dist: float = 500.0) -> Tuple[float, float]:
        rel = emitter_pos - self.position
        dist = rel.length()
        if dist >= max_dist:
            return 0.0, 0.0
        
        gain = max(0.0, 1.0 - (dist / max_dist))
        pan = max(-1.0, min(1.0, rel.x / 200.0))  # Left/Right stereo pan
        return pan, gain
