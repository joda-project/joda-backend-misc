from django.db import models

from joda_core.documents.models import Document


class MiscType(models.Model):
    name = models.CharField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.name


class MiscDocument(Document):
    misc_type = models.ForeignKey(MiscType)
