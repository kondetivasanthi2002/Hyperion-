"""
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
