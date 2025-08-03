from abc import ABC, abstractmethod
import uuid

from apps.notes.domain.entities.note import Note


class NoteRepository(ABC):
    @abstractmethod
    def exists(self, reference: uuid.UUID) -> bool:
        raise NotImplementedError("Method not implemented")

    @abstractmethod
    def get_all(self) -> list[Note]:
        raise NotImplementedError("Method not implemented")

    @abstractmethod
    def get_by_reference(self, reference: uuid.UUID) -> Note:
        raise NotImplementedError("Method not implemented")

    @abstractmethod
    def save(self, note: Note) -> None:
        raise NotImplementedError("Method not implemented")
