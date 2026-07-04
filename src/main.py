"""
PERITO-AI
Entry point of the system.
"""

from src.core.orchestrator import Orchestrator


def main():
    print("PERITO-AI starting...")

    orchestrator = Orchestrator()
    orchestrator.run()


if __name__ == "__main__":
    main()