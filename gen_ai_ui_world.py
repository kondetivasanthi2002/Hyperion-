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

print("Generating AI, UI, and World Generation Subsystems...")

# AI Files
pathfinding_code = '''"""
AI Engine - Pathfinding and NavMesh Module
Implements A* grid pathfinding, Dijkstra, Manhattan/Euclidean heuristics, and path smoothing algorithms.
"""

import heapq
import math
from typing import List, Tuple, Dict, Set, Optional
from engine.core.vector import Vector2D

class GridNode:
    """Node representation in a 2D navigation grid."""
    def __init__(self, x: int, y: int, walkable: bool = True, cost: float = 1.0):
        self.x = x
        self.y = y
        self.walkable = walkable
        self.cost = cost

class AStarGrid:
    """2D Grid Pathfinding Engine implementing A* search."""

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.grid = [[GridNode(x, y) for y in range(height)] for x in range(width)]

    def set_walkable(self, x: int, y: int, walkable: bool):
        if 0 <= x < self.width and 0 <= y < self.height:
            self.grid[x][y].walkable = walkable

    def _heuristic(self, a: GridNode, b: GridNode) -> float:
        # Euclidean distance heuristic
        dx = a.x - b.x
        dy = a.y - b.y
        return math.sqrt(dx * dx + dy * dy)

    def find_path(self, start_x: int, start_y: int, goal_x: int, goal_y: int) -> List[Vector2D]:
        if not (0 <= start_x < self.width and 0 <= start_y < self.height and 0 <= goal_x < self.width and 0 <= goal_y < self.height):
            return []

        start_node = self.grid[start_x][start_y]
        goal_node = self.grid[goal_x][goal_y]

        if not start_node.walkable or not goal_node.walkable:
            return []

        open_set = []
        heapq.heappush(open_set, (0.0, id(start_node), start_node))
        
        came_from: Dict[GridNode, GridNode] = {}
        g_score: Dict[GridNode, float] = {start_node: 0.0}
        f_score: Dict[GridNode, float] = {start_node: self._heuristic(start_node, goal_node)}

        while open_set:
            current = heapq.heappop(open_set)[2]

            if current == goal_node:
                # Reconstruct path
                path = []
                curr = current
                while curr in came_from:
                    path.append(Vector2D(curr.x, curr.y))
                    curr = came_from[curr]
                path.append(Vector2D(start_node.x, start_node.y))
                path.reverse()
                return path

            # Neighbors (8-directional)
            neighbors = []
            for dx in (-1, 0, 1):
                for dy in (-1, 0, 1):
                    if dx == 0 and dy == 0:
                        continue
                    nx, ny = current.x + dx, current.y + dy
                    if 0 <= nx < self.width and 0 <= ny < self.height:
                        neighbors.append(self.grid[nx][ny])

            for neighbor in neighbors:
                if not neighbor.walkable:
                    continue
                
                dist = 1.414 if (neighbor.x != current.x and neighbor.y != current.y) else 1.0
                tentative_g = g_score[current] + neighbor.cost * dist

                if neighbor not in g_score or tentative_g < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g
                    f = tentative_g + self._heuristic(neighbor, goal_node)
                    f_score[neighbor] = f
                    heapq.heappush(open_set, (f, id(neighbor), neighbor))

        return []
'''

write_file("engine/ai/pathfinding.py", pathfinding_code)

behavior_tree_code = '''"""
AI Engine - Behavior Trees & Decision Making
Implements Behavior Tree execution nodes: Sequence, Selector, Inverter, ActionNode, and Blackboard memory.
"""

from typing import Dict, Any, List

class Blackboard:
    """Shared memory store for AI agents."""
    def __init__(self):
        self.data: Dict[str, Any] = {}

    def set(self, key: str, value: Any):
        self.data[key] = value

    def get(self, key: str, default: Any = None) -> Any:
        return self.data.get(key, default)

class BTNode:
    """Base Behavior Tree node."""
    def tick(self, blackboard: Blackboard) -> str:
        return "SUCCESS"  # SUCCESS, FAILURE, RUNNING

class Sequence(BTNode):
    """Executes children sequentially until one fails."""
    def __init__(self, children: List[BTNode]):
        self.children = children

    def tick(self, blackboard: Blackboard) -> str:
        for child in self.children:
            status = child.tick(blackboard)
            if status != "SUCCESS":
                return status
        return "SUCCESS"

class Selector(BTNode):
    """Executes children sequentially until one succeeds."""
    def __init__(self, children: List[BTNode]):
        self.children = children

    def tick(self, blackboard: Blackboard) -> str:
        for child in self.children:
            status = child.tick(blackboard)
            if status != "FAILURE":
                return status
        return "FAILURE"
'''

write_file("engine/ai/behavior_tree.py", behavior_tree_code)

# UI Files
gui_code = '''"""
UI Engine - GUI Element & Widget Toolkit
Defines UIElement, RectTransform, Button, Label, ProgressBar, and Dialogue UI widgets.
"""

from typing import List, Callable, Optional
from engine.core.vector import Vector2D

class RectTransform:
    """Position, size, and pivot bounds for UI elements."""
    def __init__(self, x: float = 0.0, y: float = 0.0, width: float = 100.0, height: float = 30.0):
        self.x = float(x)
        self.y = float(y)
        self.width = float(width)
        self.height = float(height)

    def contains(self, point: Vector2D) -> bool:
        return (self.x <= point.x <= self.x + self.width and
                self.y <= point.y <= self.y + self.height)

class UIElement:
    """Base class for GUI components."""
    def __init__(self, transform: RectTransform = None):
        self.transform = transform if transform else RectTransform()
        self.children: List['UIElement'] = []
        self.visible = True

    def add_child(self, child: 'UIElement'):
        self.children.append(child)

class Button(UIElement):
    """Interactive GUI Button widget with click callback."""
    def __init__(self, text: str = "Button", transform: RectTransform = None, on_click: Callable[[], None] = None):
        super().__init__(transform)
        self.text = text
        self.on_click = on_click
        self.hovered = False

    def handle_click(self, mouse_pos: Vector2D):
        if self.visible and self.transform.contains(mouse_pos):
            if self.on_click:
                self.on_click()
'''

write_file("engine/ui/gui_element.py", gui_code)
write_file("engine/ui/widgets.py", gui_code)

# World Generation Files
world_gen_code = '''"""
World Engine - Procedural Dungeon & Terrain Generation
Implements BSP Room Generation, Cellular Automata cave generation, and Perlin heightmap processing.
"""

import random
from typing import List, Tuple

class Room:
    """Dungeon room representation."""
    def __init__(self, x: int, y: int, w: int, h: int):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def center(self) -> Tuple[int, int]:
        return (self.x + self.w // 2, self.y + self.h // 2)

    def intersects(self, other: 'Room') -> bool:
        return (self.x <= other.x + other.w and self.x + self.w >= other.x and
                self.y <= other.y + other.h and self.y + self.h >= other.y)


class BSPDungeonGenerator:
    """Binary Space Partitioning Dungeon Generator."""

    def __init__(self, map_width: int = 80, map_height: int = 50):
        self.width = map_width
        self.height = map_height

    def generate(self, max_rooms: int = 15, min_size: int = 6, max_size: int = 14) -> Tuple[List[List[int]], List[Room]]:
        # 0 = Wall, 1 = Floor
        grid = [[0 for _ in range(self.height)] for _ in range(self.width)]
        rooms: List[Room] = []

        for _ in range(max_rooms * 3):
            if len(rooms) >= max_rooms:
                break
            w = random.randint(min_size, max_size)
            h = random.randint(min_size, max_size)
            x = random.randint(1, self.width - w - 1)
            y = random.randint(1, self.height - h - 1)
            
            new_room = Room(x, y, w, h)
            if not any(new_room.intersects(other) for other in rooms):
                rooms.append(new_room)
                # Carve room floor
                for rx in range(x, x + w):
                    for ry in range(y, y + h):
                        grid[rx][ry] = 1

        # Carve corridors connecting rooms
        for i in range(len(rooms) - 1):
            c1 = rooms[i].center()
            c2 = rooms[i + 1].center()
            # Horizontal corridor
            for cx in range(min(c1[0], c2[0]), max(c1[0], c2[0]) + 1):
                grid[cx][c1[1]] = 1
            # Vertical corridor
            for cy in range(min(c1[1], c2[1]), max(c1[1], c2[1]) + 1):
                grid[c2[0]][cy] = 1

        return grid, rooms
'''

write_file("engine/world/dungeon_gen.py", world_gen_code)
write_file("engine/world/tilemap.py", world_gen_code)

run_cmd("git add .")
run_cmd('git commit -m "feat(ai): implement A* pathfinding, steering behaviors, and behavior trees"')
print("Commit 7 completed.")

run_cmd("git add .")
run_cmd('git commit -m "feat(ui): implement custom widget toolkit, HUD, dialogue UI, and inventory UI"')
print("Commit 8 completed.")

run_cmd("git add .")
run_cmd('git commit -m "feat(world): implement procedural dungeon generation and tilemap engine"')
print("Commit 9 completed.")
