from rest_framework_json_api import serializers

from joda_misc.models import MiscDocument, MiscType


class MiscDocumentSerializer(serializers.ModelSerializer):
    included_serializers = {
        'files': 'joda_core.files.serializers.FileSerializer'
    }

    class Meta:
        model = MiscDocument
        resource_name = 'misc-documents'
        exclude = ('polymorphic_ctype',)


class MiscTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = MiscType
        resource_name = 'misc-types'
        fields = ('id', 'name')
