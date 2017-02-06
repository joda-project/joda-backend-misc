import os
from joda.version import get_version

default_app_config = 'joda_misc.apps.MiscConfig'

version = get_version(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))

item_name = 'misc-document'
item_group = 'misc-documents'
