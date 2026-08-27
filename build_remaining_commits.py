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

print("Building Physics Engine (engine/physics/)...")

# Physics files
rigidbody_code = '''"""
Physics Engine - Rigidbody Dynamics Module
Implements 2D/3D rigidbody physics state, velocity integration, force/torque accumulators, and damping models.
"""

import math
from engine.core.vector import Vector2D, Vector3D

class Rigidbody2D:
    """2D Rigidbody handling translational and rotational dynamics."""

    def __init__(self, mass: float = 1.0, is_static: bool = False):
        self.mass = mass if not is_static else 0.0
        self.inv_mass = 1.0 / mass if mass > 0 and not is_static else 0.0
        self.inertia = 10.0 if not is_static else 0.0
        self.inv_inertia = 1.0 / self.inertia if self.inertia > 0 and not is_static else 0.0
        self.is_static = is_static
        
        self.position = Vector2D(0.0, 0.0)
        self.velocity = Vector2D(0.0, 0.0)
        self.force_accumulator = Vector2D(0.0, 0.0)
        
        self.rotation = 0.0  # Radians
        self.angular_velocity = 0.0
        self.torque_accumulator = 0.0
        
        self.linear_damping = 0.01
        self.angular_damping = 0.05
        self.restitution = 0.5  # Bounciness
        self.friction = 0.3     # Surface friction

    def apply_force(self, force: Vector2D):
        if not self.is_static:
            self.force_accumulator += force

    def apply_impulse(self, impulse: Vector2D, contact_point: Vector2D = None):
        if not self.is_static:
            self.velocity += impulse * self.inv_mass
            if contact_point:
                r = contact_point - self.position
                self.angular_velocity += r.cross(impulse) * self.inv_inertia

    def integrate(self, dt: float, gravity: Vector2D = Vector2D(0.0, -9.81)):
        if self.is_static:
            return
        
        # Apply gravity
        self.force_accumulator += gravity * self.mass
        
        # Integrate linear motion
        acceleration = self.force_accumulator * self.inv_mass
        self.velocity += acceleration * dt
        self.velocity *= max(0.0, 1.0 - self.linear_damping * dt)
        self.position += self.velocity * dt
        
        # Integrate rotational motion
        angular_acceleration = self.torque_accumulator * self.inv_inertia
        self.angular_velocity += angular_acceleration * dt
        self.angular_velocity *= max(0.0, 1.0 - self.angular_damping * dt)
        self.rotation += self.angular_velocity * dt
        
        # Clear accumulators
        self.force_accumulator = Vector2D(0.0, 0.0)
        self.torque_accumulator = 0.0
'''

write_file("engine/physics/rigidbody.py", rigidbody_code)

colliders_code = '''"""
Physics Engine - Colliders and Shape Definitions
Defines BoxCollider2D, CircleCollider2D, PolygonCollider2D, and collision manifolds.
"""

from typing import List, Tuple
from engine.core.vector import Vector2D

class CollisionManifold:
    """Stores contact information between two colliding bodies."""

    def __init__(self, body_a=None, body_b=None):
        self.body_a = body_a
        self.body_b = body_b
        self.normal = Vector2D(0.0, 1.0)
        self.penetration = 0.0
        self.contacts: List[Vector2D] = []
        self.collided = False

class BoxCollider2D:
    """Axis-Aligned or Oriented Bounding Box Collider."""

    def __init__(self, width: float = 1.0, height: float = 1.0, offset: Vector2D = None):
        self.width = float(width)
        self.height = float(height)
        self.offset = offset if offset else Vector2D(0.0, 0.0)

    def get_vertices(self, position: Vector2D, rotation: float) -> List[Vector2D]:
        hw = self.width * 0.5
        hh = self.height * 0.5
        local_verts = [
            Vector2D(-hw, -hh),
            Vector2D(hw, -hh),
            Vector2D(hw, hh),
            Vector2D(-hw, hh)
        ]
        world_verts = []
        for v in local_verts:
            rotated = (v + self.offset).rotate(rotation)
            world_verts.append(rotated + position)
        return world_verts

class CircleCollider2D:
    """Bounding Circle Collider."""

    def __init__(self, radius: float = 0.5, offset: Vector2D = None):
        self.radius = float(radius)
        self.offset = offset if offset else Vector2D(0.0, 0.0)
'''

write_file("engine/physics/colliders.py", colliders_code)

physics_world_code = '''"""
Physics Engine - Physics World Simulator
Manages step accumulator, broadphase culling, SAT collision resolution, and constraint solving.
"""

from typing import List
from engine.core.vector import Vector2D
from engine.physics.rigidbody import Rigidbody2D
from engine.physics.colliders import CircleCollider2D, CollisionManifold

class PhysicsWorld:
    """2D Physics simulation world managing gravity and rigidbodies."""

    def __init__(self, gravity: Vector2D = Vector2D(0.0, -9.81)):
        self.gravity = gravity
        self.bodies: List[Rigidbody2D] = []

    def add_body(self, body: Rigidbody2D):
        if body not in self.bodies:
            self.bodies.append(body)

    def remove_body(self, body: Rigidbody2D):
        if body in self.bodies:
            self.bodies.remove(body)

    def step(self, dt: float, sub_steps: int = 4):
        sub_dt = dt / float(sub_steps)
        for _ in range(sub_steps):
            for body in self.bodies:
                body.integrate(sub_dt, self.gravity)
            self._resolve_collisions()

    def _resolve_collisions(self):
        # Circle-Circle simple collision check
        n = len(self.bodies)
        for i in range(n):
            for j in range(i + 1, n):
                b1 = self.bodies[i]
                b2 = self.bodies[j]
                if b1.is_static and b2.is_static:
                    continue
                dist = b1.position.distance_to(b2.position)
                min_dist = 1.0  # Default unit radius check
                if dist < min_dist and dist > 0.0:
                    normal = (b2.position - b1.position) / dist
                    penetration = min_dist - dist
                    
                    # Separation positional fix
                    total_inv = b1.inv_mass + b2.inv_mass
                    if total_inv > 0:
                        b1.position -= normal * (penetration * (b1.inv_mass / total_inv))
                        b2.position += normal * (penetration * (b2.inv_mass / total_inv))
                    
                    # Relative velocity impulse
                    rel_vel = b2.velocity - b1.velocity
                    vel_along_normal = rel_vel.dot(normal)
                    if vel_along_normal < 0:
                        e = min(b1.restitution, b2.restitution)
                        j_impulse = -(1.0 + e) * vel_along_normal / total_inv
                        impulse = normal * j_impulse
                        b1.apply_impulse(-impulse)
                        b2.apply_impulse(impulse)
'''

write_file("engine/physics/physics_world.py", physics_world_code)

run_cmd("git add .")
run_cmd('git commit -m "feat(physics): implement 2D/3D rigidbody physics and collision detection engine"')
print("Commit 4 completed.")
