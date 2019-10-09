from .base import *
from .upload import *

# Local settings, here simple as is possible
# in future should be based on environment variables

try:
    from __local_settings import *
except ImportError as e:
    print(e)