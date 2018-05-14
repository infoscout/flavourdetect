# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import RequestFactory, TestCase

from flavourdetect.middleware import FlavourDetectMiddleware


class MiddlewareTestCase(TestCase):
    """
    Tests for middleware.py file with mixin
    """

    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()

    def test_process_request(self):
        # set up instance of class and pass flavour
        view_for_response_mixin = FlavourDetectMiddleware()
        request = self.factory.get('/foo?flavour=iphone')
        view_for_response_mixin.process_request(request)

        # verify request.flavour was reset from None
        self.assertEqual(request.flavour, 'IPHONE')
