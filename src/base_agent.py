"""
Base Agent - all AI agents must inherit from this class
"""


class BaseAgent:
    def __init__(self, name: str):
        self.name = name

    def run(self, context: dict) -> dict:
        raise NotImplementedError("Agents must implement run() method")