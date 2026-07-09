from src.pipelines.document_pipeline import DocumentPipeline


class PipelineEngine:

    def __init__(self):
        self.pipeline = DocumentPipeline()

    def execute(self):

        context = {
            "document": {},
            "metadata": {},
            "analysis": {},
            "report": {}
        }

        return self.pipeline.run(context)