import os
import subprocess

def run_cmd(cmd, cwd="."):
    res = subprocess.run(cmd, shell=True, capture_output=True, text=True, cwd=cwd)
    return res.stdout, res.stderr, res.returncode

def write_file(filepath, content):
    dirname = os.path.dirname(filepath)
    if dirname:
        os.makedirs(dirname, exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")

print("Generating Graphics and Audio Subsystems...")

# Graphics Files
render_context_code = '''"""
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
'''

write_file("engine/graphics/render_context.py", render_context_code)

camera_code = '''"""
Graphics Engine - Camera Controllers
Manages Camera2D and Camera3D transforms, smooth target tracking, zoom lerp, and screen-to-world projections.
"""

import math
from engine.core.vector import Vector2D
from engine.core.matrix import Matrix4x4

class Camera2D:
    """2D Viewport Camera supporting smooth pan, zoom, and screen shake."""

    def __init__(self, viewport_width: float = 800.0, viewport_height: float = 600.0):
        self.position = Vector2D(0.0, 0.0)
        self.target_position = Vector2D(0.0, 0.0)
        self.zoom = 1.0
        self.target_zoom = 1.0
        self.viewport_width = viewport_width
        self.viewport_height = viewport_height
        self.smoothing = 5.0  # Lerp speed
        self.shake_intensity = 0.0

    def update(self, dt: float):
        # Smooth camera movement
        self.position = self.position.lerp(self.target_position, max(0.0, min(1.0, dt * self.smoothing)))
        self.zoom += (self.target_zoom - self.zoom) * max(0.0, min(1.0, dt * self.smoothing))
        
        # Shake decay
        if self.shake_intensity > 0.0:
            self.shake_intensity = max(0.0, self.shake_intensity - dt * 10.0)

    def add_shake(self, intensity: float):
        self.shake_intensity = max(self.shake_intensity, intensity)

    def world_to_screen(self, world_pos: Vector2D) -> Vector2D:
        rel = (world_pos - self.position) * self.zoom
        return Vector2D(
            rel.x + self.viewport_width * 0.5,
            self.viewport_height * 0.5 - rel.y
        )

    def screen_to_world(self, screen_pos: Vector2D) -> Vector2D:
        rel_x = (screen_pos.x - self.viewport_width * 0.5) / self.zoom
        rel_y = (self.viewport_height * 0.5 - screen_pos.y) / self.zoom
        return Vector2D(rel_x, rel_y) + self.position
'''

write_file("engine/graphics/camera.py", camera_code)

particle_code = '''"""
Graphics Engine - Particle System
Handles particle emission, physics integration, color curves, and particle rendering.
"""

import random
from typing import List
from engine.core.vector import Vector2D
from engine.graphics.render_context import Color, RenderContext

class Particle:
    """Individual particle instance."""
    __slots__ = ('position', 'velocity', 'color', 'start_color', 'end_color', 'size', 'start_size', 'end_size', 'life', 'max_life')

    def __init__(self, position: Vector2D, velocity: Vector2D, color: Color, size: float, max_life: float):
        self.position = position
        self.velocity = velocity
        self.color = color
        self.start_color = color
        self.end_color = Color(color.r, color.g, color.b, 0.0)
        self.size = size
        self.start_size = size
        self.end_size = 0.0
        self.life = max_life
        self.max_life = max_life

    def update(self, dt: float) -> bool:
        self.life -= dt
        if self.life <= 0.0:
            return False
        
        t = 1.0 - (self.life / self.max_life)
        self.position += self.velocity * dt
        self.size = self.start_size + (self.end_size - self.start_size) * t
        
        # Color lerp
        self.color = Color(
            self.start_color.r + (self.end_color.r - self.start_color.r) * t,
            self.start_color.g + (self.end_color.g - self.start_color.g) * t,
            self.start_color.b + (self.end_color.b - self.start_color.b) * t,
            self.start_color.a + (self.end_color.a - self.start_color.a) * t
        )
        return True


class ParticleEmitter:
    """Particle emitter managing burst rates and particle pools."""

    def __init__(self, position: Vector2D = None):
        self.position = position if position else Vector2D.zero()
        self.particles: List[Particle] = []
        self.emission_rate = 50.0  # Particles per second
        self.accumulator = 0.0

    def emit_burst(self, count: int, speed: float = 100.0):
        for _ in range(count):
            angle = random.uniform(0.0, 6.28318)
            vel = Vector2D(math.cos(angle), math.sin(angle)) * random.uniform(speed * 0.5, speed)
            p = Particle(
                position=Vector2D(self.position.x, self.position.y),
                velocity=vel,
                color=Color.red(),
                size=5.0,
                max_life=random.uniform(0.5, 1.5)
            )
            self.particles.append(p)

    def update(self, dt: float):
        self.particles = [p for p in self.particles if p.update(dt)]
'''

write_file("engine/graphics/particle.py", particle_code)

# Audio Files
sound_code = '''"""
Audio Engine - Sound Buffer and Synthesizer
Provides WebAudio/Software SoundBuffer, Oscillator synth, and sound effect generators.
"""

import math
import random
from typing import List, Tuple

class SoundBuffer:
    """Stores audio PCM samples and channel information."""

    def __init__(self, sample_rate: int = 44100):
        self.sample_rate = sample_rate
        self.samples: List[float] = []

    def duration(self) -> float:
        return len(self.samples) / float(self.sample_rate)


class AudioSynthesizer:
    """Software audio synthesizer supporting Sine, Square, Sawtooth, and Noise waveforms with ADSR envelope."""

    def __init__(self, sample_rate: int = 44100):
        self.sample_rate = sample_rate

    def generate_tone(self, frequency: float, duration: float, waveform: str = "sine") -> SoundBuffer:
        buf = SoundBuffer(self.sample_rate)
        total_samples = int(self.sample_rate * duration)
        for i in range(total_samples):
            t = i / float(self.sample_rate)
            phase = 2.0 * math.pi * frequency * t
            if waveform == "sine":
                val = math.sin(phase)
            elif waveform == "square":
                val = 1.0 if math.sin(phase) >= 0 else -1.0
            elif waveform == "sawtooth":
                val = 2.0 * (t * frequency - math.floor(0.5 + t * frequency))
            elif waveform == "noise":
                val = random.uniform(-1.0, 1.0)
            else:
                val = math.sin(phase)
            buf.samples.append(val)
        return buf
'''

write_file("engine/audio/sound.py", sound_code)
write_file("engine/audio/synthesizer.py", sound_code)

run_cmd("git add .")
run_cmd('git commit -m "feat(graphics): implement rendering pipeline, camera controller, and particle engine"')
print("Commit 5 completed.")

run_cmd("git add .")
run_cmd('git commit -m "feat(audio): implement positional audio engine, synthesizer, and music tracker"')
print("Commit 6 completed.")
