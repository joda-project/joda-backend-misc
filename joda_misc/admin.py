from django.contrib import admin

from joda_core.documents.admin import DocumentsAdmin
from joda_misc.models import MiscDocument, MiscType


class MiscDocumentsAdmin(DocumentsAdmin):
    list_filter = ['misc_type', 'created_at', 'changed_at']
    search_fields = ['title', 'misc_type', 'notes', 'tags']


class MiscTypesAdmin(admin.ModelAdmin):
    ordering = ('name',)


admin.site.register(MiscDocument, MiscDocumentsAdmin)
admin.site.register(MiscType, MiscTypesAdmin)
