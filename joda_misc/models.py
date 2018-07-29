""" Miscellaneous documents models """

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ugettext

from joda_core.documents.models import Document


class MiscType(models.Model):
    """
    A type of miscellaneous documents
    """
    DEFAULT_PK = 1
    name = models.CharField(max_length=255, unique=True,
                            db_index=True, verbose_name=_('name'))

    class Meta:
        verbose_name = _('miscellaneous document type')
        verbose_name_plural = _('miscellaneous document types')

    class JSONAPIMeta:
        """ JSONAPIMeta """
        resource_name = 'misc-types'

    def __str__(self):
        if self.pk == self.DEFAULT_PK:
            return self.name + ' (' + ugettext('default, can not be deleted') + ')'
        return self.name


class MiscDocument(Document):
    """
    Miscellaneous document type containing no additional fields,
    except a type (MiscType)
    """
    misc_type = models.ForeignKey(
        MiscType, blank=False, on_delete=models.PROTECT, default=MiscType.DEFAULT_PK,
        verbose_name=_('miscellaneous document type'))

    class Meta:
        verbose_name = _('miscellaneous document')
        verbose_name_plural = _('miscellaneous documents')

    class JSONAPIMeta:
        """ JSONAPIMeta """
        resource_name = 'misc-documents'
