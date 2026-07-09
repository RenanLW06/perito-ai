from src.pipelines.base_pipeline import BasePipeline

from src.pipelines.stages.input_stage import InputStage
from src.pipelines.stages.validation_stage import ValidationStage
from src.pipelines.stages.ocr_stage import OCRStage
from src.pipelines.stages.structuring_stage import StructuringStage
from src.pipelines.stages.analysis_stage import AnalysisStage
from src.pipelines.stages.review_stage import ReviewStage
from src.pipelines.stages.report_stage import ReportStage


class DocumentPipeline(BasePipeline):

    def __init__(self):

        super().__init__()

        self.stages = [

            InputStage(),

            ValidationStage(),

            OCRStage(),

            StructuringStage(),

            AnalysisStage(),

            ReviewStage(),

            ReportStage()

        ]