""" Admin tests """
# pylint: disable=protected-access

from django.contrib.admin.sites import AdminSite
from django.contrib.messages.storage.fallback import FallbackStorage
from django.http.request import HttpRequest
from django.test import TestCase

from joda_core.models import User
from joda_misc.admin import MiscTypesAdmin
from joda_misc.models import MiscType


class MockRequest(HttpRequest):
    """
    Mock HttpRequest helper class
    """

    def __init__(self, user):
        HttpRequest.__init__(self)
        self.user = user
        self.session = 'session'
        self._messages = FallbackStorage(self)


class AdminTestCase(TestCase):
    """
    Test MistTypesAdmin
    """

    def setUp(self):
        self.first = MiscType.objects.get(pk=1)
        self.second = MiscType.objects.create(name='Second Type')
        self.site = AdminSite()

    def test_custom_has_delete_permission(self):
        """
        MiscTypesAdmin.has_delete_permission()
        does not allow first one to be deleted
        """
        request = MockRequest(User.objects.create_superuser(
            username='bob', email='bob@test.com', password='test'))

        self.site.register(MiscType, MiscTypesAdmin)
        ma = self.site._registry[MiscType]

        blank_result = ma.has_delete_permission(request)
        self.assertEqual(blank_result, True)

        first_result = ma.has_delete_permission(request, obj=self.first)
        self.assertEqual(first_result, False)

        second_result = ma.has_delete_permission(request, obj=self.second)
        self.assertEqual(second_result, True)
