from django.test import RequestFactory, TestCase

from flavourdetect.context_processors import flavour
from flavourdetect.flavours import Flavour


class FlavoursTestCase(TestCase):
    """
    Verify context_processors.py file functions correctly
    """

    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()

    def test_flavour(self):
        """
        Verify flavour() returns correct flavour and hierarchy
        """
        request = self.factory.get('/foo')
        request.flavour = Flavour.IPAD

        flavour_dict = flavour(request)
        self.assertDictEqual(
            flavour_dict,
            {'flavours': ['IPAD', 'IOS', 'MOBILE'], 'flavour': 'IPAD'}
        )
