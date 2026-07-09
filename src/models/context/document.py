from pydantic import BaseModel


class Document(BaseModel):

    id: str | None = None

    filename: str | None = None

    filetype: str | None = None

    status: str = "pending"

    text: str | None = None