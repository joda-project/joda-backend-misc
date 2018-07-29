""" Initialisation tests """

from django.test import TestCase

import joda_misc


class InitTestCase(TestCase):
    """ Test Initialisation """

    def test_meta(self):
        """Test meta information"""
        self.assertEqual(joda_misc.model_name, 'MiscDocument')
        self.assertEqual(joda_misc.item_name, 'misc-document')
        self.assertEqual(joda_misc.item_group, 'misc-documents')
