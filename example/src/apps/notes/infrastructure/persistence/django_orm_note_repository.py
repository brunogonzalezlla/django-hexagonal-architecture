import uuid

from apps.notes.application.ports.note_repository import NoteRepository
from apps.notes.domain.entities.note import Note
from apps.notes.domain.exceptions.note import NoteNotFoundError
from apps.notes.infrastructure.orm.models import Note as NoteModel


class DjangoORMNoteRepository(NoteRepository):
    def __init__(self):
        self.model = NoteModel

    def exists(self, reference: uuid.UUID) -> bool:
        return self.model.objects.filter(reference=reference).exists()

    def get_all(self) -> list[Note]:
        notes = self.model.objects.all()
        return [note.to_entity() for note in notes]

    def get_by_reference(self, reference: str) -> Note:
        try:
            note_model = self.model.objects.get(reference=reference)
            return note_model.to_entity()
        except self.model.DoesNotExist:
            raise NoteNotFoundError(reference)

    def save(self, note: Note) -> None:
        try:
            note_model = self.model.objects.get(reference=note.reference)
            note_model.title = note.title
            note_model.content = note.content
            note_model.save()
        except self.model.DoesNotExist:
            note_model = self.model.from_entity(note)

        note_model.save()
