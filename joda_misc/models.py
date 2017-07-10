from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ugettext as _u

from joda_core.documents.models import Document


class MiscType(models.Model):
    DEFAULT_PK = 1
    name = models.CharField(max_length=255, unique=True,
                            db_index=True, verbose_name=_('name'))

    class Meta:
        verbose_name = _('miscellaneous document type')
        verbose_name_plural = _('miscellaneous document types')

    class JSONAPIMeta:
        resource_name = 'misc-types'

    def __str__(self):
        if self.pk == self.DEFAULT_PK:
            return self.name + ' (' + _u('default, can not be deleted') + ')'
        return self.name


class MiscDocument(Document):
    misc_type = models.ForeignKey(
        MiscType, blank=False, default=MiscType.DEFAULT_PK,
        verbose_name=_('miscellaneous document type'))

    class Meta:
        verbose_name = _('miscellaneous document')
        verbose_name_plural = _('miscellaneous documents')

    class JSONAPIMeta:
        resource_name = 'misc-documents'
