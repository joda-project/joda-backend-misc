from rest_framework import filters, viewsets

from joda_misc.models import MiscDocument, MiscType
from joda_misc.serializers import MiscDocumentSerializer, MiscTypeSerializer


class MiscDocumentsViewSet(viewsets.ModelViewSet):
    serializer_class = MiscDocumentSerializer
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter)
    filter_fields = ('misc_type', 'tags', 'public', 'verified')
    search_fields = ('title', 'tags__name')

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return MiscDocument.objects.filter(public=True).order_by('-pk')
        return MiscDocument.objects.order_by('-pk')


class MiscTypesViewSet(viewsets.ModelViewSet):
    queryset = MiscType.objects.all().order_by('name')
    serializer_class = MiscTypeSerializer
