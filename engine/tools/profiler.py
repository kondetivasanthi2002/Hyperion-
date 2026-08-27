"""
Tools Engine - Level Editor & Profiler Gizmos
Implements visual level editor tools, scene profiler, draw call tracker, and debug wireframe rendering.
"""

from typing import Dict

class PerformanceProfiler:
    """Tracks frame times, draw calls, and memory usage."""

    def __init__(self):
        self.frame_time = 0.0
        self.fps = 60.0
        self.draw_calls = 0
        self.entity_count = 0

    def record_frame(self, dt: float, draw_calls: int, entity_count: int):
        self.frame_time = dt
        self.fps = 1.0 / dt if dt > 0 else 60.0
        self.draw_calls = draw_calls
        self.entity_count = entity_count
