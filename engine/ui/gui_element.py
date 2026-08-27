"""
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
