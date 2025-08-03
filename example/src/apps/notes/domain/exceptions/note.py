class NoteNotFoundError(Exception):
    """Exception raised when a note is not found in the system."""
    def __init__(self, reference: str):
        super().__init__(f"Note with reference '{reference}' not found.")
        self.reference = reference
