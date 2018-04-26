from django.core.exceptions import ImproperlyConfigured
from django.test import RequestFactory, TestCase

from flavourdetect.utils import FlavourTemplateResponseMixin


class TemplateViewTestCase(TestCase):
    """
    Test FlavourTemplateResponseMixin from utils.py
    """

    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()

    def test_get_template_names(self):
        """
        Verify FlavourTemplateResponseMixin responds correctly when
        template_name present or not
        """

        class FooView(FlavourTemplateResponseMixin):
            template_name = None

        # test error raised when no template_name
        view_without_template_name = FooView()
        with self.assertRaises(ImproperlyConfigured):
            view_without_template_name.get_template_names()

        # test no error when template_name is present
        view_with_template_name = FooView()
        view_with_template_name.template_name = 'template_name'
        view_with_template_name.request = self.factory.get('/foo')
        templates = view_with_template_name.get_template_names()
        self.assertEqual(templates, ['template_name'])
