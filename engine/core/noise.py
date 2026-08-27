"""
Core Math Engine - Procedural Noise Module
Implements 2D/3D Perlin Noise, Simplex Noise, Fractal Brownian Motion (fBm), and Worley Noise for world generator.
"""

import math
import random
from typing import List, Tuple


class PerlinNoise:
    """Gradient-based 2D and 3D Perlin Noise generator."""

    def __init__(self, seed: int = 1337):
        self.seed = seed
        self.p = list(range(256))
        rnd = random.Random(seed)
        rnd.shuffle(self.p)
        self.p = self.p + self.p

    def _fade(self, t: float) -> float:
        return t * t * t * (t * (t * 6 - 15) + 10)

    def _lerp(self, t: float, a: float, b: float) -> float:
        return a + t * (b - a)

    def _grad2d(self, hash_val: int, x: float, y: float) -> float:
        h = hash_val & 7
        u = x if h < 4 else y
        v = y if h < 4 else x
        return (u if (h & 1) == 0 else -u) + (v if (h & 2) == 0 else -v)

    def noise2d(self, x: float, y: float) -> float:
        xi = int(math.floor(x)) & 255
        yi = int(math.floor(y)) & 255
        xf = x - math.floor(x)
        yf = y - math.floor(y)

        u = self._fade(xf)
        v = self._fade(yf)

        aa = self.p[self.p[xi] + yi]
        ab = self.p[self.p[xi] + yi + 1]
        ba = self.p[self.p[xi + 1] + yi]
        bb = self.p[self.p[xi + 1] + yi + 1]

        x1 = self._lerp(u, self._grad2d(aa, xf, yf), self._grad2d(ba, xf - 1, yf))
        x2 = self._lerp(u, self._grad2d(ab, xf, yf - 1), self._grad2d(bb, xf - 1, yf - 1))
        return self._lerp(v, x1, x2)

    def fbm2d(self, x: float, y: float, octaves: int = 4, persistence: float = 0.5, lacunarity: float = 2.0) -> float:
        total = 0.0
        frequency = 1.0
        amplitude = 1.0
        max_val = 0.0
        for _ in range(octaves):
            total += self.noise2d(x * frequency, y * frequency) * amplitude
            max_val += amplitude
            amplitude *= persistence
            frequency *= lacunarity
        return total / max_val if max_val > 0 else 0.0
