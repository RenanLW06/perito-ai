from pydantic import BaseModel


class Metadata(BaseModel):

    case_number: str | None = None

    court: str | None = None

    expert_name: str | None = None

    created_at: str | None = None