from django.test import RequestFactory, TestCase

from flavourdetect.utils import flavour_detect, template_list


class UtilsTestCase(TestCase):
    """
    Testing utils.py file
    """

    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()

    def test_flavour_detect(self):
        """
        Verify correct flavor returned after get request
        """
        # testing flavour passed but no user_agent present
        request = self.factory.get('/foo?flavour=iphone')
        flavour = flavour_detect(request)
        self.assertEqual(flavour, 'IPHONE')

        # testing no flavour passed
        request = self.factory.get('/foo')
        flavour = flavour_detect(request)
        self.assertIsNone(flavour)

        # testing specific user agents
        request = self.factory.get('/foo', HTTP_USER_AGENT='IPOD')
        flavour = flavour_detect(request)
        self.assertEqual(flavour, 'IPOD')

        request = self.factory.get('/foo', HTTP_USER_AGENT='IPHONE')
        flavour = flavour_detect(request)
        self.assertEqual(flavour, 'IPHONE')

        request = self.factory.get('/foo', HTTP_USER_AGENT='BLACKBERRY')
        flavour = flavour_detect(request)
        self.assertEqual(flavour, 'BLACKBERRY')

        request = self.factory.get('/foo', HTTP_USER_AGENT='ANDROID')
        flavour = flavour_detect(request)
        self.assertEqual(flavour, 'ANDROID')

        request = self.factory.get('/foo', HTTP_USER_AGENT='IPAD')
        flavour = flavour_detect(request)
        self.assertEqual(flavour, 'IPAD')

    def test_template_list(self):
        """
        Verify template_list returns correct heirarchy
        """
        # test flavour passed in request
        request = self.factory.get('/foo?flavour=ipad')
        templates = template_list(request, 'template_name')
        self.assertEqual(
            templates,
            [
                'template_name-ipad',
                'template_name-ios',
                'template_name-mobile',
                'template_name',
            ]
        )

        # test no flavour passed in request
        request = self.factory.get('/foo')
        templates = template_list(request, 'template_name')
        self.assertEqual(templates, ['template_name'])
