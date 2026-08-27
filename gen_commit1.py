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

# Project Setup
readme_content = """# Hyperion Game Development Engine & RPG Application

Hyperion is a high-performance, modular 2D/3D Game Engine and RPG Application written in Python. It features a complete custom math library, Entity-Component-System (ECS) framework, impulse-based physics solver, software/canvas rendering pipeline, positional WebAudio/synthesizer sound engine, A* pathfinding and behavior trees, a rich GUI component library, procedural world generation, turn-based/real-time combat mechanics, inventory & quest engines, in-game level editor, and comprehensive automated test suites.

## Engine Architecture Subsystems

- **Core Math Engine (`engine/core/`)**: Vectors, matrices, quaternions, noise generators, bounding volumes, splines, transform hierarchies.
- **ECS Framework (`engine/ecs/`)**: High-performance Entity-Component-System with query caching, bitmask filtering, and archetype storage.
- **Physics Engine (`engine/physics/`)**: 2D/3D rigidbody dynamics, SAT/GJK collision detection, impulse constraint solver, joint constraints.
- **Graphics Pipeline (`engine/graphics/`)**: Canvas & WebGL rendering abstractions, camera controllers, particle emitters, dynamic lighting, post-processing filters.
- **Audio Synthesizer (`engine/audio/`)**: Oscillator sound synthesizer, ADSR envelopes, procedural SFX generator, music step tracker, spatial audio.
- **AI & Pathfinding (`engine/ai/`)**: A* grid pathfinding, NavMesh generator, steering behaviors, Behavior Trees, Utility AI.
- **UI Framework (`engine/ui/`)**: RectTransform GUI widget system, HUD manager, dialogue box typewriter, inventory grid, skill tree editor.
- **Procedural World Engine (`engine/world/`)**: BSP dungeon generator, cellular automata caves, Perlin noise terrain, infinite chunking manager.
- **Gameplay Mechanics (`engine/gameplay/`)**: RPG stats, skill trees, combat resolution, crafting engine, quest manager, JSON save/load serialization.
- **Developer Tools (`engine/tools/`)**: Embedded visual level editor, scene inspector, performance profiler, debug drawing gizmos.
- **Automated Test Suites (`tests/`)**: Unit & integration test suites covering math, ecs, physics, ai, gameplay, and serialization.

## Quick Start

### Counting Lines of Code (LOC)
```bash
python scripts/count_loc.py
```

### Running Automated Test Suites
```bash
python -m unittest discover tests
```

### Launching the Application & Game Engine
```bash
python main.py
```
"""

gitignore_content = """__pycache__/
*.pyc
*.pyo
*.pyd
.pytest_cache/
.coverage
htmlcov/
dist/
build/
*.egg-info/
.DS_Store
*.log
.vscode/
.idea/
"""

pyproject_content = """[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"

[project]
name = "hyperion-game-engine"
version = "1.0.0"
description = "A 50k+ LOC modular Game Engine & RPG Application"
readme = "README.md"
requires-python = ">=3.10"
dependencies = []
"""

count_loc_script = """import os

def count_lines(directory="."):
    total_files = 0
    total_lines = 0
    total_code = 0
    total_comments = 0
    total_blank = 0

    print("=" * 60)
    print(f"{'Module Path':<35} | {'Files':<6} | {'Lines':<8}")
    print("=" * 60)

    for root, dirs, files in os.walk(directory):
        if any(ignored in root for ignored in [".git", "__pycache__", ".venv", "build", "dist"]):
            continue
        
        py_files = [f for f in files if f.endswith(".py")]
        if not py_files:
            continue
        
        module_lines = 0
        for file in py_files:
            filepath = os.path.join(root, file)
            try:
                with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
                    lines = f.readlines()
                    module_lines += len(lines)
                    for line in lines:
                        stripped = line.strip()
                        if not stripped:
                            total_blank += 1
                        elif stripped.startswith("#"):
                            total_comments += 1
                        else:
                            total_code += 1
            except Exception as e:
                pass
        
        total_files += len(py_files)
        total_lines += module_lines
        rel_root = os.path.relpath(root, directory)
        print(f"{rel_root:<35} | {len(py_files):<6} | {module_lines:<8}")

    print("=" * 60)
    print(f"Total Python Files : {total_files}")
    print(f"Total Lines of Code: {total_lines}")
    print(f"  - Executable Code : {total_code}")
    print(f"  - Comments        : {total_comments}")
    print(f"  - Blank Lines     : {total_blank}")
    print("=" * 60)

if __name__ == "__main__":
    count_lines(".")
"""

main_script = """import sys
import os

from engine.core.vector import Vector2D
from engine.ecs.world import World
from engine.physics.physics_world import PhysicsWorld
from engine.gameplay.stats import StatBlock

def main():
    print("==================================================")
    print(" Hyperion 50k+ LOC Game Engine & RPG Application  ")
    print("==================================================")
    print("Initializing Core Engine Subsystems...")
    
    world = World()
    physics = PhysicsWorld()
    player_stats = StatBlock(health=100, mana=50, strength=15, agility=12, intelligence=10)
    
    print(f"[OK] ECS World Initialized: {world}")
    print(f"[OK] Physics World Initialized: {physics}")
    print(f"[OK] Player Stats Initialized: HP={player_stats.health}, MP={player_stats.mana}")
    print("Engine initialization completed successfully!")

if __name__ == "__main__":
    main()
"""

write_file("README.md", readme_content)
write_file(".gitignore", gitignore_content)
write_file("pyproject.toml", pyproject_content)
write_file("scripts/count_loc.py", count_loc_script)

run_cmd("git add .")
run_cmd('git commit -m "init: initial repository layout, build configuration, and testing setup"')
print("Commit 1 completed.")
