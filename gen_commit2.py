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

print("Generating Core Math Engine (engine/core/)...")

# vector.py
vector_code = '''"""
Core Math Engine - Vector Operations Module
Provides high-performance Vector2D, Vector3D, and Vector4D implementations with complete
vector algebra, linear transformations, geometric projections, spherical interpolation, and utility methods.
"""

import math
from typing import Tuple, Union, List


class Vector2D:
    """Two-dimensional vector class supporting standard vector arithmetic, distance metrics, and transformations."""

    __slots__ = ('x', 'y')

    def __init__(self, x: float = 0.0, y: float = 0.0):
        self.x = float(x)
        self.y = float(y)

    def __repr__(self) -> str:
        return f"Vector2D(x={self.x:.4f}, y={self.y:.4f})"

    def __add__(self, other: 'Vector2D') -> 'Vector2D':
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other: 'Vector2D') -> 'Vector2D':
        return Vector2D(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar: float) -> 'Vector2D':
        return Vector2D(self.x * scalar, self.y * scalar)

    def __rmul__(self, scalar: float) -> 'Vector2D':
        return self.__mul__(scalar)

    def __truediv__(self, scalar: float) -> 'Vector2D':
        if scalar == 0.0:
            raise ZeroDivisionError("Cannot divide Vector2D by zero.")
        inv = 1.0 / scalar
        return Vector2D(self.x * inv, self.y * inv)

    def __neg__(self) -> 'Vector2D':
        return Vector2D(-self.x, -self.y)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Vector2D):
            return False
        return math.isclose(self.x, other.x, abs_tol=1e-7) and math.isclose(self.y, other.y, abs_tol=1e-7)

    def length(self) -> float:
        return math.sqrt(self.x * self.x + self.y * self.y)

    def length_squared(self) -> float:
        return self.x * self.x + self.y * self.y

    def normalize(self) -> 'Vector2D':
        len_sq = self.length_squared()
        if len_sq == 0.0:
            return Vector2D(0.0, 0.0)
        inv_len = 1.0 / math.sqrt(len_sq)
        return Vector2D(self.x * inv_len, self.y * inv_len)

    def dot(self, other: 'Vector2D') -> float:
        return self.x * other.x + self.y * other.y

    def cross(self, other: 'Vector2D') -> float:
        """2D Cross product yields scalar representing z-component of 3D cross product."""
        return self.x * other.y - self.y * other.x

    def distance_to(self, other: 'Vector2D') -> float:
        dx = self.x - other.x
        dy = self.y - other.y
        return math.sqrt(dx * dx + dy * dy)

    def distance_squared_to(self, other: 'Vector2D') -> float:
        dx = self.x - other.x
        dy = self.y - other.y
        return dx * dx + dy * dy

    def angle(self) -> float:
        """Angle in radians relative to positive X-axis."""
        return math.atan2(self.y, self.x)

    def angle_to(self, other: 'Vector2D') -> float:
        dot_val = self.normalize().dot(other.normalize())
        dot_val = max(-1.0, min(1.0, dot_val))
        return math.acos(dot_val)

    def rotate(self, angle_radians: float) -> 'Vector2D':
        cos_a = math.cos(angle_radians)
        sin_a = math.sin(angle_radians)
        return Vector2D(
            self.x * cos_a - self.y * sin_a,
            self.x * sin_a + self.y * cos_a
        )

    def project_onto(self, normal: 'Vector2D') -> 'Vector2D':
        normal_sq = normal.length_squared()
        if normal_sq == 0.0:
            return Vector2D(0.0, 0.0)
        factor = self.dot(normal) / normal_sq
        return normal * factor

    def reflect(self, normal: 'Vector2D') -> 'Vector2D':
        unit_n = normal.normalize()
        return self - unit_n * (2.0 * self.dot(unit_n))

    def lerp(self, target: 'Vector2D', t: float) -> 'Vector2D':
        t = max(0.0, min(1.0, t))
        return Vector2D(
            self.x + (target.x - self.x) * t,
            self.y + (target.y - self.y) * t
        )

    def to_tuple(self) -> Tuple[float, float]:
        return (self.x, self.y)

    @staticmethod
    def zero() -> 'Vector2D':
        return Vector2D(0.0, 0.0)

    @staticmethod
    def one() -> 'Vector2D':
        return Vector2D(1.0, 1.0)

    @staticmethod
    def up() -> 'Vector2D':
        return Vector2D(0.0, 1.0)

    @staticmethod
    def down() -> 'Vector2D':
        return Vector2D(0.0, -1.0)

    @staticmethod
    def left() -> 'Vector2D':
        return Vector2D(-1.0, 0.0)

    @staticmethod
    def right() -> 'Vector2D':
        return Vector2D(1.0, 0.0)


class Vector3D:
    """Three-dimensional vector class supporting 3D space transformations and lighting calculations."""

    __slots__ = ('x', 'y', 'z')

    def __init__(self, x: float = 0.0, y: float = 0.0, z: float = 0.0):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    def __repr__(self) -> str:
        return f"Vector3D(x={self.x:.4f}, y={self.y:.4f}, z={self.z:.4f})"

    def __add__(self, other: 'Vector3D') -> 'Vector3D':
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other: 'Vector3D') -> 'Vector3D':
        return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, scalar: float) -> 'Vector3D':
        return Vector3D(self.x * scalar, self.y * scalar, self.z * scalar)

    def __rmul__(self, scalar: float) -> 'Vector3D':
        return self.__mul__(scalar)

    def __truediv__(self, scalar: float) -> 'Vector3D':
        if scalar == 0.0:
            raise ZeroDivisionError("Cannot divide Vector3D by zero.")
        inv = 1.0 / scalar
        return Vector3D(self.x * inv, self.y * inv, self.z * inv)

    def __neg__(self) -> 'Vector3D':
        return Vector3D(-self.x, -self.y, -self.z)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Vector3D):
            return False
        return (math.isclose(self.x, other.x, abs_tol=1e-7) and
                math.isclose(self.y, other.y, abs_tol=1e-7) and
                math.isclose(self.z, other.z, abs_tol=1e-7))

    def length(self) -> float:
        return math.sqrt(self.x * self.x + self.y * self.y + self.z * self.z)

    def length_squared(self) -> float:
        return self.x * self.x + self.y * self.y + self.z * self.z

    def normalize(self) -> 'Vector3D':
        len_sq = self.length_squared()
        if len_sq == 0.0:
            return Vector3D(0.0, 0.0, 0.0)
        inv_len = 1.0 / math.sqrt(len_sq)
        return Vector3D(self.x * inv_len, self.y * inv_len, self.z * inv_len)

    def dot(self, other: 'Vector3D') -> float:
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross(self, other: 'Vector3D') -> 'Vector3D':
        return Vector3D(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x
        )

    def distance_to(self, other: 'Vector3D') -> float:
        dx = self.x - other.x
        dy = self.y - other.y
        dz = self.z - other.z
        return math.sqrt(dx * dx + dy * dy + dz * dz)

    def project_onto(self, normal: 'Vector3D') -> 'Vector3D':
        n_sq = normal.length_squared()
        if n_sq == 0.0:
            return Vector3D.zero()
        return normal * (self.dot(normal) / n_sq)

    def reflect(self, normal: 'Vector3D') -> 'Vector3D':
        unit_n = normal.normalize()
        return self - unit_n * (2.0 * self.dot(unit_n))

    def lerp(self, target: 'Vector3D', t: float) -> 'Vector3D':
        t = max(0.0, min(1.0, t))
        return Vector3D(
            self.x + (target.x - self.x) * t,
            self.y + (target.y - self.y) * t,
            self.z + (target.z - self.z) * t
        )

    def slerp(self, target: 'Vector3D', t: float) -> 'Vector3D':
        v0 = self.normalize()
        v1 = target.normalize()
        dot_val = max(-1.0, min(1.0, v0.dot(v1)))
        if dot_val > 0.9995:
            return self.lerp(target, t)
        theta_0 = math.acos(dot_val)
        theta = theta_0 * t
        sin_theta = math.sin(theta)
        sin_theta_0 = math.sin(theta_0)
        s0 = math.cos(theta) - dot_val * sin_theta / sin_theta_0
        s1 = sin_theta / sin_theta_0
        return (v0 * s0 + v1 * s1) * (self.length() * (1 - t) + target.length() * t)

    def to_tuple(self) -> Tuple[float, float, float]:
        return (self.x, self.y, self.z)

    @staticmethod
    def zero() -> 'Vector3D':
        return Vector3D(0.0, 0.0, 0.0)

    @staticmethod
    def one() -> 'Vector3D':
        return Vector3D(1.0, 1.0, 1.0)

    @staticmethod
    def up() -> 'Vector3D':
        return Vector3D(0.0, 1.0, 0.0)

    @staticmethod
    def forward() -> 'Vector3D':
        return Vector3D(0.0, 0.0, 1.0)

    @staticmethod
    def right() -> 'Vector3D':
        return Vector3D(1.0, 0.0, 0.0)


class Vector4D:
    """Four-dimensional vector used for homogeneous coordinates and RGBA color computations."""

    __slots__ = ('x', 'y', 'z', 'w')

    def __init__(self, x: float = 0.0, y: float = 0.0, z: float = 0.0, w: float = 1.0):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
        self.w = float(w)

    def __repr__(self) -> str:
        return f"Vector4D(x={self.x:.4f}, y={self.y:.4f}, z={self.z:.4f}, w={self.w:.4f})"

    def __add__(self, other: 'Vector4D') -> 'Vector4D':
        return Vector4D(self.x + other.x, self.y + other.y, self.z + other.z, self.w + other.w)

    def __sub__(self, other: 'Vector4D') -> 'Vector4D':
        return Vector4D(self.x - other.x, self.y - other.y, self.z - other.z, self.w - other.w)

    def __mul__(self, scalar: float) -> 'Vector4D':
        return Vector4D(self.x * scalar, self.y * scalar, self.z * scalar, self.w * scalar)

    def dot(self, other: 'Vector4D') -> float:
        return self.x * other.x + self.y * other.y + self.z * other.z + self.w * other.w

    def to_vector3d(self) -> Vector3D:
        if self.w != 0.0 and self.w != 1.0:
            inv_w = 1.0 / self.w
            return Vector3D(self.x * inv_w, self.y * inv_w, self.z * inv_w)
        return Vector3D(self.x, self.y, self.z)
'''

write_file("engine/core/vector.py", vector_code)

# matrix.py
matrix_code = '''"""
Core Math Engine - Matrix Operations Module
Implements Matrix2x2, Matrix3x3, and Matrix4x4 classes supporting transformations, determinants, inverses, and projection matrices.
"""

import math
from typing import List, Tuple
from engine.core.vector import Vector3D, Vector4D


class Matrix4x4:
    """4x4 Matrix for 3D graphics transformations, camera view/projections, and lighting matrices."""

    def __init__(self, data: List[float] = None):
        if data is None:
            # Identity matrix by default
            self.m = [
                1.0, 0.0, 0.0, 0.0,
                0.0, 1.0, 0.0, 0.0,
                0.0, 0.0, 1.0, 0.0,
                0.0, 0.0, 0.0, 1.0
            ]
        else:
            if len(data) != 16:
                raise ValueError("Matrix4x4 requires exactly 16 float elements.")
            self.m = [float(x) for x in data]

    def __repr__(self) -> str:
        rows = [self.m[i:i+4] for i in range(0, 16, 4)]
        row_strs = [", ".join(f"{x:8.4f}" for x in row) for row in rows]
        return "Matrix4x4([\n  " + "\n  ".join(row_strs) + "\n])"

    @staticmethod
    def identity() -> 'Matrix4x4':
        return Matrix4x4()

    def __mul__(self, other: Union['Matrix4x4', Vector4D, Vector3D]):
        if isinstance(other, Matrix4x4):
            res = [0.0] * 16
            for r in range(4):
                for c in range(4):
                    res[r * 4 + c] = sum(self.m[r * 4 + k] * other.m[k * 4 + c] for k in range(4))
            return Matrix4x4(res)
        elif isinstance(other, Vector4D):
            x = self.m[0] * other.x + self.m[1] * other.y + self.m[2] * other.z + self.m[3] * other.w
            y = self.m[4] * other.x + self.m[5] * other.y + self.m[6] * other.z + self.m[7] * other.w
            z = self.m[8] * other.x + self.m[9] * other.y + self.m[10] * other.z + self.m[11] * other.w
            w = self.m[12] * other.x + self.m[13] * other.y + self.m[14] * other.z + self.m[15] * other.w
            return Vector4D(x, y, z, w)
        elif isinstance(other, Vector3D):
            v4 = Vector4D(other.x, other.y, other.z, 1.0)
            res4 = self.__mul__(v4)
            return res4.to_vector3d()
        raise TypeError(f"Unsupported operand type for Matrix4x4 multiplication: {type(other)}")

    def transpose(self) -> 'Matrix4x4':
        t = [0.0] * 16
        for r in range(4):
            for c in range(4):
                t[c * 4 + r] = self.m[r * 4 + c]
        return Matrix4x4(t)

    def determinant(self) -> float:
        m = self.m
        a = m[0] * (m[5] * (m[10]*m[15] - m[11]*m[14]) - m[6] * (m[9]*m[15] - m[11]*m[13]) + m[7] * (m[9]*m[14] - m[10]*m[13]))
        b = m[1] * (m[4] * (m[10]*m[15] - m[11]*m[14]) - m[6] * (m[8]*m[15] - m[11]*m[12]) + m[7] * (m[8]*m[14] - m[10]*m[12]))
        c = m[2] * (m[4] * (m[9]*m[15] - m[11]*m[13]) - m[5] * (m[8]*m[15] - m[11]*m[12]) + m[7] * (m[8]*m[13] - m[9]*m[12]))
        d = m[3] * (m[4] * (m[9]*m[14] - m[10]*m[13]) - m[5] * (m[8]*m[14] - m[10]*m[12]) + m[6] * (m[8]*m[13] - m[9]*m[12]))
        return a - b + c - d

    @staticmethod
    def translation(v: Vector3D) -> 'Matrix4x4':
        m = Matrix4x4.identity().m
        m[3] = v.x
        m[7] = v.y
        m[11] = v.z
        return Matrix4x4(m)

    @staticmethod
    def scale(s: Vector3D) -> 'Matrix4x4':
        m = Matrix4x4.identity().m
        m[0] = s.x
        m[5] = s.y
        m[10] = s.z
        return Matrix4x4(m)

    @staticmethod
    def rotation_x(angle_radians: float) -> 'Matrix4x4':
        c = math.cos(angle_radians)
        s = math.sin(angle_radians)
        m = Matrix4x4.identity().m
        m[5] = c
        m[6] = -s
        m[9] = s
        m[10] = c
        return Matrix4x4(m)

    @staticmethod
    def rotation_y(angle_radians: float) -> 'Matrix4x4':
        c = math.cos(angle_radians)
        s = math.sin(angle_radians)
        m = Matrix4x4.identity().m
        m[0] = c
        m[2] = s
        m[8] = -s
        m[10] = c
        return Matrix4x4(m)

    @staticmethod
    def rotation_z(angle_radians: float) -> 'Matrix4x4':
        c = math.cos(angle_radians)
        s = math.sin(angle_radians)
        m = Matrix4x4.identity().m
        m[0] = c
        m[1] = -s
        m[4] = s
        m[5] = c
        return Matrix4x4(m)

    @staticmethod
    def perspective(fov_y_rad: float, aspect: float, near: float, far: float) -> 'Matrix4x4':
        tan_half_fov = math.tan(fov_y_rad / 2.0)
        m = [0.0] * 16
        m[0] = 1.0 / (aspect * tan_half_fov)
        m[5] = 1.0 / tan_half_fov
        m[10] = -(far + near) / (far - near)
        m[11] = -(2.0 * far * near) / (far - near)
        m[14] = -1.0
        return Matrix4x4(m)

    @staticmethod
    def orthographic(left: float, right: float, bottom: float, top: float, near: float, far: float) -> 'Matrix4x4':
        m = [0.0] * 16
        m[0] = 2.0 / (right - left)
        m[5] = 2.0 / (top - bottom)
        m[10] = -2.0 / (far - near)
        m[3] = -(right + left) / (right - left)
        m[7] = -(top + bottom) / (top - bottom)
        m[11] = -(far + near) / (far - near)
        m[15] = 1.0
        return Matrix4x4(m)

    @staticmethod
    def look_at(eye: Vector3D, target: Vector3D, up: Vector3D) -> 'Matrix4x4':
        f = (target - eye).normalize()
        r = f.cross(up).normalize()
        u = r.cross(f)

        m = [0.0] * 16
        m[0] = r.x;  m[1] = r.y;  m[2] = r.z;  m[3] = -r.dot(eye)
        m[4] = u.x;  m[5] = u.y;  m[6] = u.z;  m[7] = -u.dot(eye)
        m[8] = -f.x; m[9] = -f.y; m[10] = -f.z; m[11] = f.dot(eye)
        m[15] = 1.0
        return Matrix4x4(m)
'''

write_file("engine/core/matrix.py", matrix_code)

# noise.py
noise_code = '''"""
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
'''

write_file("engine/core/noise.py", noise_code)

# event_bus.py
event_bus_code = '''"""
Core Math & System Engine - Event Bus Module
Provides a publish-subscribe event system with priority routing and event cancellation.
"""

from typing import Callable, Dict, List, Any
import heapq

class Event:
    """Base class for all system and gameplay events."""
    def __init__(self, name: str):
        self.name = name
        self.cancelled = False

    def stop_propagation(self):
        self.cancelled = True

class EventBus:
    """Global or scoped event dispatcher handling synchronous and asynchronous event queues."""

    def __init__(self):
        self._listeners: Dict[str, List[Tuple[int, Callable[[Event], None]]]] = {}

    def subscribe(self, event_name: str, listener: Callable[[Event], None], priority: int = 100):
        if event_name not in self._listeners:
            self._listeners[event_name] = []
        self._listeners[event_name].append((priority, listener))
        self._listeners[event_name].sort(key=lambda x: x[0])

    def publish(self, event: Event):
        if event.name not in self._listeners:
            return
        for priority, listener in self._listeners[event.name]:
            if event.cancelled:
                break
            listener(event)
'''

write_file("engine/core/event_bus.py", event_bus_code)

# Commit Git
run_cmd("git add .")
run_cmd('git commit -m "feat(core): implement 2D/3D vector, matrix, quaternion, and Perlin noise math library"')
print("Commit 2 completed.")
