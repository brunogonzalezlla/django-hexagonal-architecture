from dependency_injector.wiring import Provide, inject
from rest_framework import status, viewsets
from rest_framework.request import Request
from rest_framework.response import Response

from apps.notes.application.services.note_service import NoteService
from apps.notes.domain.exceptions.note import NoteNotFoundError
from apps.notes.interfaces.serializers import CreateOrUpdateNoteSerializer, NoteSerializer
from apps.notes.interfaces.serializers import NoteSerializer
from config.container import Container


class NoteViewSet(viewsets.ViewSet):
    @inject
    def list(
        self,
        request: Request,
        note_service: NoteService = Provide[Container.note_service],
    ):
        """
        Retrieve all notes.
        """
        notes = note_service.get_all_notes()
        serializer = NoteSerializer(notes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @inject
    def retrieve(
        self,
        request: Request,
        pk,
        note_service: NoteService = Provide[Container.note_service],
    ):
        """
        Retrieve a note by its reference.
        """
        reference = pk
        try:
            note = note_service.get_note_by_reference(reference)
            serializer = NoteSerializer(note)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except NoteNotFoundError:
            return Response(
                {"error": "Note not found."}, status=status.HTTP_404_NOT_FOUND
            )

    @inject
    def create(
        self,
        request: Request,
        note_service: NoteService = Provide[Container.note_service],
    ):
        """
        Create a new note.
        """
        serializer = CreateOrUpdateNoteSerializer(data=request.data)
        if serializer.is_valid():
            note = note_service.create_note(**serializer.validated_data)
            return Response(
                NoteSerializer(note).data, status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @inject
    def update(
        self,
        request: Request,
        pk,
        note_service: NoteService = Provide[Container.note_service],
    ):
        """
        Update an existing note.
        """
        reference = pk
        serializer = CreateOrUpdateNoteSerializer(data=request.data)
        if serializer.is_valid():
            try:
                note = note_service.update_note(
                    reference, **serializer.validated_data
                )
                return Response(
                    NoteSerializer(note).data, status=status.HTTP_200_OK
                )
            except NoteNotFoundError:
                return Response(
                    {"error": "Note not found."}, status=status.HTTP_404_NOT_FOUND
                )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @inject
    def delete(
        self,
        request: Request,
        pk,
        note_service: NoteService = Provide[Container.note_service],
    ):
        """
        Delete a note by its reference.
        """
        reference = pk
        try:
            note_service.note_repository.delete(reference)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except NoteNotFoundError:
            return Response(
                {"error": "Note not found."}, status=status.HTTP_404_NOT_FOUND
            )
