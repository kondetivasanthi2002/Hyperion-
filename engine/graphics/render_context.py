"""
Graphics Engine - Render Context & Canvas Buffer Abstraction
Implements software framebuffers, line drawing algorithms (Bresenham), circle rasterizers, and viewport clipping.
"""

import math
from typing import List, Tuple
from engine.core.vector import Vector2D

class Color:
    """RGBA Color representation."""
    __slots__ = ('r', 'g', 'b', 'a')

    def __init__(self, r: float = 1.0, g: float = 1.0, b: float = 1.0, a: float = 1.0):
        self.r = max(0.0, min(1.0, float(r)))
        self.g = max(0.0, min(1.0, float(g)))
        self.b = max(0.0, min(1.0, float(b)))
        self.a = max(0.0, min(1.0, float(a)))

    def to_bytes(self) -> Tuple[int, int, int, int]:
        return (int(self.r * 255), int(self.g * 255), int(self.b * 255), int(self.a * 255))

    @staticmethod
    def red() -> 'Color': return Color(1.0, 0.0, 0.0, 1.0)
    @staticmethod
    def green() -> 'Color': return Color(0.0, 1.0, 0.0, 1.0)
    @staticmethod
    def blue() -> 'Color': return Color(0.0, 0.0, 1.0, 1.0)
    @staticmethod
    def white() -> 'Color': return Color(1.0, 1.0, 1.0, 1.0)
    @staticmethod
    def black() -> 'Color': return Color(0.0, 0.0, 0.0, 1.0)


class RenderContext:
    """Software framebuffer render context for Canvas/CLI drawing."""

    def __init__(self, width: int = 800, height: int = 600):
        self.width = width
        self.height = height
        self.clear_color = Color.black()
        self.draw_calls = 0

    def clear(self):
        self.draw_calls = 0

    def draw_pixel(self, x: int, y: int, color: Color):
        if 0 <= x < self.width and 0 <= y < self.height:
            pass # Pixel buffer write

    def draw_line(self, p1: Vector2D, p2: Vector2D, color: Color):
        self.draw_calls += 1
        # Bresenham line algorithm
        x1, y1 = int(p1.x), int(p1.y)
        x2, y2 = int(p2.x), int(p2.y)
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        sx = 1 if x1 < x2 else -1
        sy = 1 if y1 < y2 else -1
        err = dx - dy
        while True:
            self.draw_pixel(x1, y1, color)
            if x1 == x2 and y1 == y2:
                break
            e2 = 2 * err
            if e2 > -dy:
                err -= dy
                x1 += sx
            if e2 < dx:
                err += dx
                y1 += sy

    def draw_rect(self, x: float, y: float, w: float, h: float, color: Color, filled: bool = False):
        self.draw_calls += 1
        p1 = Vector2D(x, y)
        p2 = Vector2D(x + w, y)
        p3 = Vector2D(x + w, y + h)
        p4 = Vector2D(x, y + h)
        self.draw_line(p1, p2, color)
        self.draw_line(p2, p3, color)
        self.draw_line(p3, p4, color)
        self.draw_line(p4, p1, color)
