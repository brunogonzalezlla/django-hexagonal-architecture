from dependency_injector import containers, providers

from apps.notes.application.services.note_service import NoteService
from apps.notes.infrastructure.persistence.django_orm_note_repository import (
    DjangoORMNoteRepository,
)
from config import settings


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    note_repository = providers.Singleton(DjangoORMNoteRepository)

    note_service = providers.Factory(
        NoteService, note_repository=note_repository
    )


container = Container()
container.config.from_dict(settings.__dict__)
