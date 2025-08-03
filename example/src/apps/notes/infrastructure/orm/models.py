from django.db import models

from apps.notes.domain.entities.note import Note as NoteDomain


class Note(models.Model):
    reference = models.UUIDField(unique=True, primary_key=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Note {self.title}"

    @classmethod
    def from_entity(cls, entity: NoteDomain) -> "Note":
        return cls(
            reference=entity.reference, title=entity.title, content=entity.content
        )

    def to_entity(self) -> NoteDomain:
        return NoteDomain(
            reference=self.reference, title=self.title, content=self.content, created_at=self.created_at
        )
