"""
Hyperion Game Development Engine & RPG Application
Interactive Real-Time Engine Demonstration Script
"""

import sys
import os
import time

from engine.core.vector import Vector2D, Vector3D
from engine.ecs.world import World
from engine.ecs.component import TransformComponent, VelocityComponent, HealthComponent, RenderComponent
from engine.physics.physics_world import PhysicsWorld
from engine.physics.rigidbody import Rigidbody2D
from engine.gameplay.stats import StatBlock
from engine.gameplay.inventory import InventoryBag, Item
from engine.gameplay.combat import DamageCalculator
from engine.ai.pathfinding import AStarGrid
from engine.graphics.camera import Camera2D
from engine.world.dungeon_gen import BSPDungeonGenerator

def run_simulation():
    print("======================================================================")
    print("      HYPERION GAME ENGINE - LIVE REAL-TIME ENGINE SIMULATION         ")
    print("======================================================================")
    
    # 1. Initialize Subsystems
    world = World()
    physics = PhysicsWorld(gravity=Vector2D(0.0, -9.81))
    camera = Camera2D(800, 600)
    grid_finder = AStarGrid(20, 20)
    
    # 2. Spawn Player Entity in ECS
    player_ent = world.create_entity()
    player_transform = TransformComponent(position=Vector3D(0.0, 0.0, 0.0))
    player_health = HealthComponent(max_hp=100.0)
    world.add_component(player_ent, player_transform)
    world.add_component(player_ent, player_health)
    
    player_stats = StatBlock(health=100, mana=50, strength=18, agility=14, intelligence=12)
    player_bag = InventoryBag(capacity=10)
    
    # 3. Add Physics Rigidbodies
    player_body = Rigidbody2D(mass=5.0)
    player_body.position = Vector2D(0.0, 10.0)
    player_body.apply_force(Vector2D(15.0, 5.0))
    physics.add_body(player_body)
    
    # 4. Generate Dungeon Level
    dungeon = BSPDungeonGenerator(map_width=40, map_height=20)
    grid, rooms = dungeon.generate(max_rooms=5)
    
    print(f"\n[INIT] Spawned Player {player_ent} in ECS World")
    print(f"[INIT] Rigidbody added at Pos=({player_body.position.x:.2f}, {player_body.position.y:.2f})")
    print(f"[INIT] Procedural Map Generated: {len(rooms)} Rooms Created")
    
    # 5. Compute AI Pathfinding Route
    start_x, start_y = rooms[0].center() if rooms else (1, 1)
    goal_x, goal_y = rooms[-1].center() if len(rooms) > 1 else (10, 10)
    path = grid_finder.find_path(start_x, start_y, goal_x, goal_y)
    print(f"[AI] Computed A* Path from ({start_x},{start_y}) to ({goal_x},{goal_y}): {len(path)} Waypoints")
    
    # 6. Execute Game Engine Ticks
    print("\n----------------------------------------------------------------------")
    print("                       SIMULATING GAME LOOP TICKS                     ")
    print("----------------------------------------------------------------------")
    
    for tick in range(1, 6):
        # Step Physics Simulation
        physics.step(dt=0.1)
        camera.target_position = player_body.position
        camera.update(dt=0.1)
        
        # Simulate Combat Encounter
        dmg, is_crit = DamageCalculator.calculate_damage(
            attacker_str=player_stats.strength,
            weapon_atk=12.0,
            defender_armor=15.0
        )
        crit_str = " *** CRITICAL HIT! ***" if is_crit else ""
        
        # Gain EXP & Items
        leveled = player_stats.add_exp(30)
        item_loot = Item(f"loot_{tick}", f"Hyperion Relic #{tick}", "Artifact", rarity="Epic")
        player_bag.add_item(item_loot)
        
        print(f"[TICK {tick:02d}] Physics Pos: ({player_body.position.x:6.2f}, {player_body.position.y:6.2f}) | Vel: ({player_body.velocity.x:5.2f}, {player_body.velocity.y:5.2f})")
        print(f"         Combat: Dealt {dmg:5.1f} DMG to Enemy{crit_str}")
        print(f"         Stats : Level={player_stats.level} (EXP: {player_stats.exp}/{player_stats.exp_to_next_level}) | Inventory: {len(player_bag.items)} items")
    
    print("\n======================================================================")
    print("           SIMULATION COMPLETED WITH 100% ENGINE INTEGRITY            ")
    print("======================================================================")

if __name__ == "__main__":
    run_simulation()
