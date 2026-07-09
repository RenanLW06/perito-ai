from src.core.context_manager import ContextManager
from src.pipelines.document_pipeline import DocumentPipeline


class PipelineEngine:

    def __init__(self):

        self.pipeline = DocumentPipeline()

    def execute(self):

        context = ContextManager()

        self.pipeline.run(context)

        context.finish()

        return context.to_dict()