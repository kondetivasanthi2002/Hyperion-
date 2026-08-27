"""
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
        return "Matrix4x4([
  " + "
  ".join(row_strs) + "
])"

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
