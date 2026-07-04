"""
Document Service
Handles document-related operations
"""


class DocumentService:
    def load_document(self, path: str):
        print(f"Loading document: {path}")
        return {"content": "dummy"}