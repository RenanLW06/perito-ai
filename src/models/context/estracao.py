from pydantic import BaseModel


class ExtractedData(BaseModel):

    tables: list = []

    values: list = []

    entities: list = []
from pydantic import BaseModel


class Analysis(BaseModel):

    summary: str | None = None

    inconsistencies: list = []

    calculations: list = []
from pydantic import BaseModel


class Report(BaseModel):

    generated: bool = False

    path: str | None = None

    content: str | None = None
from pydantic import BaseModel


class Audit(BaseModel):

    events: list = []
from pydantic import BaseModel


class Execution(BaseModel):

    started_at: str | None = None

    finished_at: str | None = None

    current_stage: str | None = None