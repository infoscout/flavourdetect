# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from flavourdetect.utils import all_flavours


def flavour(request):
    # Skip context processor if FlavourDetectMiddleware has not executed yet
    if not hasattr(request, 'flavour'):
        return {}

    # Add the flavour and all flavours to the context
    flavour = request.flavour
    return {
        'flavour': flavour,
        'flavours': all_flavours(flavour),
    }
