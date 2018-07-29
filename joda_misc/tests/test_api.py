""" API tests """

from django.conf.urls import include, url
from django.urls import reverse
from django.test import override_settings, TestCase

from rest_framework import status
from rest_framework.test import APIClient

from joda_core.models import User
from joda_misc.models import MiscDocument, MiscType
from joda_misc.router import router as MiscRouter


class TestUrlConf:
    """
    Test URLs config
    """
    urlpatterns = [url('', include(MiscRouter.urls))]


@override_settings(ROOT_URLCONF=TestUrlConf)
class APITests(TestCase):
    """
    Test miscellaneous documents API
    """

    def setUp(self):
        self.client = APIClient()

    def test_list_misc_types(self):
        """
        Test listing miscellaneous documents types
        """
        MiscType.objects.create(name='Test Documents')
        MiscType.objects.create(name='ABC Documents')

        path = reverse('misctype-list')
        request = self.client.get(path)

        self.assertEqual(request.status_code, status.HTTP_200_OK)
        self.assertEqual(len(request.data), 3)
        self.assertEqual(request.data[0]['name'], 'ABC Documents')

    def test_list_misc_documents(self):
        """
        Test listing miscellaneous documents
        """
        MiscDocument.objects.create(title='Public Document', public=True)
        MiscDocument.objects.create(title='Private Document')

        path = reverse('misc-documents-list')

        request_public = self.client.get(path)
        self.assertEqual(request_public.status_code, status.HTTP_200_OK)
        self.assertEqual(len(request_public.data['results']), 1)
        self.assertEqual(
            request_public.data['results'][0]['title'], 'Public Document')

        self.client.force_authenticate(
            User.objects.get_or_create(username='testuser')[0])

        request_private = self.client.get(path)
        self.assertEqual(request_private.status_code, status.HTTP_200_OK)
        self.assertEqual(len(request_private.data['results']), 2)
        self.assertEqual(
            request_private.data['results'][0]['title'], 'Private Document')
