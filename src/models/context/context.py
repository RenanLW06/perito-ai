from pydantic import BaseModel

from .metadata import Metadata
from .document import Document
from .extracted_data import ExtractedData
from .analysis import Analysis
from .report import Report
from .audit import Audit
from .execution import Execution


class ExecutionContext(BaseModel):

    metadata: Metadata = Metadata()

    document: Document = Document()

    extracted_data: ExtractedData = ExtractedData()

    analysis: Analysis = Analysis()

    report: Report = Report()

    audit: Audit = Audit()

    execution: Execution = Execution()

    logs: list = []

    errors: list = []

    metrics: dict = {}