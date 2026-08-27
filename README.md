# Hyperion Game Development Engine & RPG Application

Hyperion is a high-performance, modular 2D/3D Game Engine and RPG Application written in Python. It features a complete custom math library, Entity-Component-System (ECS) framework, impulse-based physics solver, software/canvas rendering pipeline, positional WebAudio/synthesizer sound engine, A* pathfinding and behavior trees, a rich GUI component library, procedural world generation, turn-based/real-time combat mechanics, inventory & quest engines, in-game level editor, and comprehensive automated test suites.

---

## Dependencies

- **Python**: `Python >= 3.10`
- **Standard Library Modules**: `math`, `os`, `sys`, `unittest`, `random`, `heapq`, `json`, `subprocess`, `http.server`
- **Frontend Dependencies**: Modern Web Browser with HTML5 Canvas API and WebAudio API support
- **Package Manifest**: `pyproject.toml`, `requirements.txt`
- **Lockfile**: `package-lock.json`

---

## Installation

To set up the Hyperion Game Engine development environment on your local machine:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/kondetivasanthi2002/Hyperion-.git
   cd Hyperion-
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Linux/macOS
   # OR on Windows:
   venv\Scripts\activate
   ```

3. **Install required dependencies**:
   ```bash
   pip install -r requirements.txt
   npm install
   ```

---

## Build

To build and package the Hyperion Game Engine library and wheel package:

1. **Build source distribution and wheel**:
   ```bash
   python -m build
   ```

2. **Install local package in editable mode**:
   ```bash
   pip install -e .
   ```

---

## Run

### 1. Launch Main Application Engine
```bash
python main.py
```

### 2. Execute Real-Time Engine Simulation
```bash
python run_demo.py
```

### 3. Launch Local Web Dashboard
```bash
python -m http.server 8000
```
Then open your browser at [http://localhost:8000/](http://localhost:8000/).

### 4. Execute Automated Test Suites
```bash
python -m unittest discover tests
# OR using pytest:
pytest tests/
```

### 5. Count Lines of Code (LOC)
```bash
python scripts/count_loc.py
```

---

## Usage

- **Player Movement**: Use <kbd>W</kbd> <kbd>A</kbd> <kbd>S</kbd> <kbd>D</kbd> or Arrow Keys to navigate inside the dungeon map.
- **Attack Action**: Press <kbd>SPACEBAR</kbd> or click `⚔️ Attack` to fire Pink Energy Slashes at enemies.
- **Special Skills**:
  - <kbd>1</kbd> **⚡ Nova**: AoE Pink Shockwave dealing 45 damage to all surrounding enemies.
  - <kbd>2</kbd> **💨 Dash**: Instant directional teleport boost.
  - <kbd>3</kbd> **💖 Heal Surge**: Consumes MP to restore +40 HP.
- **Equipment System**: Click items in your Inventory Bag to equip them into active Weapon, Armor, or Ring slots. Click equipped items to return them to your bag.
- **Merchant Shop**: Defeat enemies to earn Gold Coins, then click `🛒 Merchant Shop` to purchase mythic weapons, dragon shields, and health elixirs.

---

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
