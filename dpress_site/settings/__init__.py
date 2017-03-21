try:
    from .local import *  # NOQA
except ImportError:
    from .dev import *  # NOQA
