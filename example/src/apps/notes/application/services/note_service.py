from datetime import datetime
from apps.notes.application.ports.note_repository import NoteRepository
from apps.notes.domain.entities.note import Note
from apps.notes.domain.exceptions.note import NoteNotFoundError
from apps.notes.domain.services.generate_reference import generate_reference


class NoteService:
    def __init__(self, note_repository: NoteRepository):
        self.note_repository = note_repository

    def get_all_notes(self) -> list[Note]:
        """
        Retrieves all notes.

        :return: A list of Note instances.
        """
        return self.note_repository.get_all()

    def get_note_by_reference(self, reference: str) -> Note:
        """
        Retrieves a note by its reference.

        :param reference: The reference of the note.
        :return: A Note instance.
        :raises NoteNotFoundError: If the note is not found.
        """
        note = self.note_repository.get_by_reference(reference)
        return note

    def create_note(self, title: str, content: str) -> Note:
        """
        Creates a new note.

        :param title: The title of the note.
        :param content: The content of the note.
        :return: A Note instance.
        """
        reference = generate_reference()
        note = Note(reference=reference, title=title, content=content)
        self.note_repository.save(note)
        return note

    def update_note(
        self, reference: str, title: str, content: str
    ) -> Note:
        """
        Updates an existing note.

        :param reference: The reference of the note to update.
        :param title: The new title of the note.
        :param content: The new content of the note.
        :return: The updated Note instance.
        :raises NoteNotFoundError: If the note is not found.
        """
        if not self.note_repository.exists(reference):
            raise NoteNotFoundError(reference)
        note = Note(reference=reference, title=title, content=content)
        self.note_repository.save(note)
        return note
