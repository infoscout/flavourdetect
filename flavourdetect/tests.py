from mock import Mock
from flavourdetect.utils import *
from flavourdetect.middleware import *
from flavourdetect.context_processors import flavour
from django.test import TestCase, RequestFactory


class FlavoursTest(TestCase):
    """
        Verify context_processors.py file functions correctly
    """
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()

    def tearDown(self):
        del self.factory

    def test_flavour(self):
        """
            Verify flavour() returns correct flavour and heirarchy
        """
        request = self.factory.get('/foo')
        request.flavour = Flavour.IPAD

        response = flavour(request)
        self.assertDictEqual(response, {'flavours': ['IPAD', 'IOS', 'MOBILE'],
                                        'flavour': 'IPAD'})

class UtilsTest(TestCase):
    """
        Testing utils.py file
    """
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()

    def tearDown(self):
        del self.factory

    def test_flavour_detect(self):
        """
            Verify correct flavor returned after get request
        """
        # testing flavour passed but no user_agent present
        request = self.factory.get('/foo?flavour=iphone')

        response = flavour_detect(request)
        self.assertEqual(response, 'IPHONE')

        # testing no flavour passed
        request = self.factory.get('/foo')

        response = flavour_detect(request)
        self.assertEqual(response, None)

        # testing specific user agents
        request = self.factory.get('/foo', HTTP_USER_AGENT='IPOD')

        response = flavour_detect(request)
        self.assertEqual(response, 'IPOD')

        request = self.factory.get('/foo', HTTP_USER_AGENT='IPHONE')

        response = flavour_detect(request)
        self.assertEqual(response, 'IPHONE')

        request = self.factory.get('/foo', HTTP_USER_AGENT='BLACKBERRY')

        response = flavour_detect(request)
        self.assertEqual(response, 'BLACKBERRY')

        request = self.factory.get('/foo', HTTP_USER_AGENT='ANDROID')

        response = flavour_detect(request)
        self.assertEqual(response, 'ANDROID')

        request = self.factory.get('/foo', HTTP_USER_AGENT='IPAD')

        response = flavour_detect(request)
        self.assertEqual(response, 'IPAD')

    def test_template_list(self):
        """
            Verify template_list returns correct heirarchy
        """
        request = self.factory.get('/foo?flavour=ipad')

        response = template_list(request, 'template_name')
        self.assertEqual(response, ['template_name-ipad', 'template_name-ios',
                                    'template_name-mobile', 'template_name'])

        # test no flavour passed in request
        request = self.factory.get('/foo')
        response = template_list(request, 'template_name')
        self.assertEqual(response, ['template_name'])

    # remove
    # def test_flavour_render(self):
    #     """
    #         Verify flavour_render passes arg[0]
    #     """
    #     request = self.factory.get('/foo?flavour=ipad')
    #     response = flavour_render(request, 'template_name')
    #     self.assertEqual(response, ['template_name-ipad', 'template_name-ios',
    #                                 'template_name-mobile', 'template_name'])

class TemplateViewTest(TestCase):
    """
        Test FlavourTemplateResponseMixin from utils.py
    """
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()

    def tearDown(self):
        del self.factory

    def test_get_template_names(self):

        class FooView(FlavourTemplateResponseMixin):
            template_name = None
            request = self.factory.get('/foo')

        # test error raised when no template_name
        g = FooView()
        with self.assertRaises(ImproperlyConfigured):
            g.get_template_names()

        # test no error when template_name is present
        k = FooView()
        k.template_name = 'template_name'
        response = k.get_template_names()

        self.assertEqual(response, ['template_name'])

class MiddlewareTest(TestCase):
    """
        Tests for middleware.py file
    """
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()

    def tearDown(self):
        del self.factory

    def test_process_request(self):

        class FooView(FlavourDetectMiddleware):
            pass

        # set up instance of class and pass flavour
        g = FooView()
        request = self.factory.get('/foo?flavour=iphone')
        g.process_request(request)

        # verify request.flavour was reset from None
        self.assertEqual(request.flavour, 'IPHONE')
