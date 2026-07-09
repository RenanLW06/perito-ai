"""
Context Manager

Centraliza o estado compartilhado durante a execução
de um pipeline do PERITO-AI.
"""

from __future__ import annotations

from copy import deepcopy
from datetime import datetime
from typing import Any


class ContextManager:
    """
    Responsável por armazenar e gerenciar o estado do pipeline.
    """

    def __init__(self) -> None:

        self._context = {

            "metadata": {},

            "document": {},

            "extracted_data": {},

            "analysis": {},

            "report": {},

            "audit": {

                "events": []

            },

            "logs": [],

            "errors": [],

            "metrics": {},

            "execution": {

                "started_at": datetime.utcnow().isoformat(),

                "finished_at": None,

                "current_stage": None

            }

        }

    # -----------------------------------------------------

    def get(self) -> dict:
        """Retorna uma cópia segura do contexto."""

        return deepcopy(self._context)

    # -----------------------------------------------------

    def section(self, name: str):

        return self._context.setdefault(name, {})

    # -----------------------------------------------------

    def update(self, section: str, data: dict):

        self._context.setdefault(section, {})

        self._context[section].update(data)

    # -----------------------------------------------------

    def set_stage(self, stage: str):

        self._context["execution"]["current_stage"] = stage

        self.add_event(f"Stage started: {stage}")

    # -----------------------------------------------------

    def add_event(self, message: str):

        self._context["audit"]["events"].append({

            "timestamp": datetime.utcnow().isoformat(),

            "message": message

        })

    # -----------------------------------------------------

    def add_log(self, message: str):

        self._context["logs"].append({

            "timestamp": datetime.utcnow().isoformat(),

            "message": message

        })

    # -----------------------------------------------------

    def add_error(self, message: str):

        self._context["errors"].append({

            "timestamp": datetime.utcnow().isoformat(),

            "message": message

        })

    # -----------------------------------------------------

    def metric(self, name: str, value: Any):

        self._context["metrics"][name] = value

    # -----------------------------------------------------

    def finish(self):

        self._context["execution"]["finished_at"] = datetime.utcnow().isoformat()

        self.add_event("Pipeline finished.")

    # -----------------------------------------------------

    def to_dict(self):

        return deepcopy(self._context)