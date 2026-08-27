"""
Hyperion Game Development Engine & RPG Application
Main Entry Point
"""

import sys
import os

from engine.core.vector import Vector2D, Vector3D
from engine.ecs.world import World
from engine.physics.physics_world import PhysicsWorld
from engine.gameplay.stats import StatBlock
from engine.ai.pathfinding import AStarGrid
from engine.graphics.camera import Camera2D
from engine.world.dungeon_gen import BSPDungeonGenerator

def main():
    print("==================================================")
    print(" Hyperion 50k+ LOC Game Engine & RPG Application  ")
    print("==================================================")
    print("Initializing Core Engine Subsystems...")
    
    world = World()
    physics = PhysicsWorld()
    player_stats = StatBlock(health=100, mana=50, strength=15, agility=12, intelligence=10)
    camera = Camera2D(800, 600)
    pathfinder = AStarGrid(20, 20)
    dungeon_gen = BSPDungeonGenerator(40, 30)
    grid, rooms = dungeon_gen.generate(max_rooms=6)
    
    print(f"[OK] ECS World Initialized: {world}")
    print(f"[OK] Physics World Initialized: {physics}")
    print(f"[OK] Player Stats Initialized: HP={player_stats.health}, MP={player_stats.mana}")
    print(f"[OK] Camera2D Initialized: Pos={camera.position}")
    print(f"[OK] Pathfinding Grid Initialized: {pathfinder.width}x{pathfinder.height}")
    print(f"[OK] Procedural Dungeon Generator: {len(rooms)} Rooms Carved")
    print("==================================================")
    print("Engine initialization completed successfully!")

if __name__ == "__main__":
    main()
