# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from flavourdetect.utils import all_flavours


def flavour(request):
    return {
        'flavour': request.flavour,
        'flavours': all_flavours(request.flavour),
    }
