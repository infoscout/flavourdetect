import os.path

from django.core.exceptions import ImproperlyConfigured
from django.shortcuts import render
from django.views.generic.base import TemplateResponseMixin

from flavourdetect.flavours import Flavour, flavour_parents


def flavour_detect(request):
    """
    Provided request object, return device flavour.
    Looks against HTTP_USER_AGENT to determine flavour.
    If GET param provided, flavour is overriden

    Enhancements:
        More sophisticated user_agent detect logic
    """

    # Check first if manually provided as GET param
    if request.GET.get('flavour'):
        return request.GET.get('flavour').upper()

    if 'HTTP_USER_AGENT' not in request.META:
        return None

    user_agent = request.META['HTTP_USER_AGENT'].lower()

    # Currently has very simple user_agent detect logic
    if 'iphone' in user_agent:
        return Flavour.IPHONE
    if 'ipad' in user_agent:
        return Flavour.IPAD
    if 'ipod' in user_agent:
        return Flavour.IPOD
    if 'android' in user_agent:
        return Flavour.ANDROID
    if 'blackberry' in user_agent:
        return Flavour.BLACKBERRY


def template_list(request, template_name):
    """
    Provided a template name, returns a list of
    template_names in priority order based on the
    request flavour.

    For example if the flavour is 'IPAD', list of
    templates may be:
    [*-ipad.html, *-ios.html, *-ios.html, *.html]
    """

    # First get flavour
    flavour = getattr(request, 'flavour', None)
    if not flavour:
        flavour = flavour_detect(request)

    # If no flavour, just return base template name
    if not flavour:
        return [template_name]

    # Append flavour (and all parent flavours) to list
    templates = []
    filename, ext = os.path.splitext(template_name)
    flavours = all_flavours(flavour)
    for flavour in flavours:
        templates.append(u'%s-%s%s' % (filename, flavour.lower(), ext))

    # Add original template
    templates.append(template_name)

    return templates


def all_flavours(flavour):
    """
    Returns the flavour and it's parents
    as a list
    """
    l = [flavour]
    _flavour = flavour
    while(True):
        if _flavour not in flavour_parents:
            break
        _flavour = flavour_parents[_flavour]
        l.append(_flavour)

    return l


def flavour_render(request, *args, **kwargs):
    """
    Wrapper for the render() django call. Appends
    flavour templates
    """
    args = list(args)
    args[0] = template_list(request, args[0])

    return render(request, *args, **kwargs)


class FlavourTemplateResponseMixin(TemplateResponseMixin):
    """
    Wrapper for TemplateResponseMixIn class. Appends flavour templates
    """

    def get_template_names(self):
        """
        Returns a list of template names to be used for the request.
        Must return a list. May not be called if render_to_response is overridden.
        """

        if self.template_name is None:
            raise ImproperlyConfigured(
                "TemplateResponseMixin requires either a definition of "
                "'template_name' or an implementation of 'get_template_names()'"
            )
        else:
            return template_list(self.request, self.template_name)
