from joda_misc.models import MiscDocument, MiscType


def create_from_upload(f, user):
    misc_type = MiscType.objects.get(pk=1)
    document = MiscDocument(title='New Miscellaneous Document', created_by=user, misc_type=misc_type)
    document.save()
    document.files.add(f)
    document.save()
    return document
