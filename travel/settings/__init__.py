from .production import *

try:
    from .local import *
except Exception as e:
    print(e)
    pass
