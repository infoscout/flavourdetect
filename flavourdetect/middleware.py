# -*- coding: utf-8 -*-
from __future__ import unicode_literals


try:
    from django.utils.deprecation import MiddlewareMixin
except ImportError:  # Django < 1.10 support
    MiddlewareMixin = object

from flavourdetect.utils import flavour_detect


class FlavourDetectMiddleware(MiddlewareMixin):

    def process_request(self, request):
        request.flavour = flavour_detect(request)
