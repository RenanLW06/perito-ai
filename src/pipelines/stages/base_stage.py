from abc import ABC, abstractmethod


class BaseStage(ABC):
    """
    Classe base para todas as etapas do pipeline.
    """

    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def execute(self, context: dict) -> dict:
        """
        Executa a etapa.

        Parameters
        ----------
        context : dict
            Contexto compartilhado do pipeline.

        Returns
        -------
        dict
            Contexto atualizado.
        """
        pass