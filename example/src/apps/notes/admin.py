from django.contrib import admin

from apps.notes.infrastructure.orm.models import Note


admin.site.register(Note)
