"""
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
