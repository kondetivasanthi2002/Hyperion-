"""
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
