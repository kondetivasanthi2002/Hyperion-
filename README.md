# Hyperion Game Development Engine & RPG Application

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
