"""Automated Test Suite 1: Core Math Engine Tests"""
import unittest
from engine.core.vector import Vector2D, Vector3D
from engine.core.matrix import Matrix4x4

class TestCoreMath(unittest.TestCase):
    def test_vector2d_addition(self):
        v1 = Vector2D(3.0, 4.0)
        v2 = Vector2D(1.0, 2.0)
        res = v1 + v2
        self.assertEqual(res.x, 4.0)
        self.assertEqual(res.y, 6.0)

    def test_vector2d_length_and_normalize(self):
        v = Vector2D(3.0, 4.0)
        self.assertEqual(v.length(), 5.0)
        norm = v.normalize()
        self.assertAlmostEqual(norm.length(), 1.0)

    def test_vector3d_cross_product(self):
        v1 = Vector3D(1.0, 0.0, 0.0)
        v2 = Vector3D(0.0, 1.0, 0.0)
        cross = v1.cross(v2)
        self.assertEqual(cross, Vector3D(0.0, 0.0, 1.0))

    def test_matrix4x4_identity_multiplication(self):
        m = Matrix4x4.identity()
        v = Vector3D(5.0, -2.0, 3.0)
        res = m * v
        self.assertEqual(res, v)

if __name__ == '__main__':
    unittest.main()
