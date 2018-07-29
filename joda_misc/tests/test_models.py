""" Models tests """

from django.test import TestCase
from django.utils import translation

from joda_misc.models import MiscType


class ModelsTestCase(TestCase):
    """
    Test MistTypesAdmin
    """

    def setUp(self):
        self.first = MiscType.objects.get(pk=1)
        self.second = MiscType.objects.create(name='Second Type')

    def test_str(self):
        """
        Test proper __str__ output
        """

        self.assertEqual(self.first.__str__(),
                         'Miscellaneous (default, can not be deleted)')

        with translation.override('sl'):
            self.assertEqual(self.first.__str__(),
                             'Miscellaneous (privzeto, ni mogoče izbrisati)')

        self.assertEqual(self.second.__str__(), 'Second Type')
