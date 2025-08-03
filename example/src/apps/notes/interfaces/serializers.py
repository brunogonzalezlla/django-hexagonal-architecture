from rest_framework import serializers


class NoteSerializer(serializers.Serializer):
    reference = serializers.UUIDField()
    title = serializers.CharField(max_length=100)
    content = serializers.CharField()
    created_at = serializers.DateTimeField(format="%Y-%m-%dT%H:%M:%S", read_only=True)


class CreateOrUpdateNoteSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    content = serializers.CharField()
