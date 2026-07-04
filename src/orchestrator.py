"""
Central Orchestrator of PERITO-AI
"""

from src.core.pipeline_engine import PipelineEngine


class Orchestrator:
    def __init__(self):
        self.pipeline_engine = PipelineEngine()

    def run(self):
        print("Orchestrator running pipeline...")

        result = self.pipeline_engine.execute()

        print("Pipeline finished:", result)