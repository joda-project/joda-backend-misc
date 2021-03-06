import os
from django.utils.translation import ugettext_lazy as _

VERSION = (0, 1, 0, 'alpha', 1)

default_app_config = 'joda_misc.apps.MiscConfig'
module_path = os.path.dirname(os.path.abspath(__file__))

model_name = 'MiscDocument'
item_name = 'misc-document'
item_group = 'misc-documents'
new_item_str = _('New Miscellaneous Document')
