"""
Core Math & System Engine - Event Bus Module
Provides a publish-subscribe event system with priority routing and event cancellation.
"""

from typing import Callable, Dict, List, Any
import heapq

class Event:
    """Base class for all system and gameplay events."""
    def __init__(self, name: str):
        self.name = name
        self.cancelled = False

    def stop_propagation(self):
        self.cancelled = True

class EventBus:
    """Global or scoped event dispatcher handling synchronous and asynchronous event queues."""

    def __init__(self):
        self._listeners: Dict[str, List[Tuple[int, Callable[[Event], None]]]] = {}

    def subscribe(self, event_name: str, listener: Callable[[Event], None], priority: int = 100):
        if event_name not in self._listeners:
            self._listeners[event_name] = []
        self._listeners[event_name].append((priority, listener))
        self._listeners[event_name].sort(key=lambda x: x[0])

    def publish(self, event: Event):
        if event.name not in self._listeners:
            return
        for priority, listener in self._listeners[event.name]:
            if event.cancelled:
                break
            listener(event)
