from django.contrib import admin

from joda_misc.models import MiscDocument, MiscType


class MiscDocumentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_filter = ['created_at', 'misc_type']
    search_fields = ['title', 'misc_type', 'tags']
    filter_horizontal = ['tags']


class MiscTypesAdmin(admin.ModelAdmin):
    ordering = ('name',)


admin.site.register(MiscDocument, MiscDocumentsAdmin)
admin.site.register(MiscType, MiscTypesAdmin)
