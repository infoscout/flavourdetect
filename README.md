# FlavourDetect

Django app helping detect the user device and serving up the appropriate template.


### Detecting the device

The `HTTP_USER_AGENT` header is parsed to detect the users device. It will return a value from the class provided in `flavourdetect.flavours`.

In addition to returning a single flavour, a heirarchy of flavours is defined in `flavourdetect.flavours`. For example: IPHONE => IOS => MOBILE. To return all parent flavours, run:

    from flavourdetect.utils import all_flavours
    from flavourdetect.flavours import Flavour

    iphone_flavour = Flavour.IPHONE
    flavours = all_flavours(iphone_flavour)
    if Flavour.MOBILE in flavours:
        ...

#### Overriding the flavour

You can append `?flavour=X` as a GET param to override and test a different flavour.


### Serving up device specific template

You can define multiple templates for a single view and dynamically serve up the correct template based on the users device. For example, a common file structure may be:

    page.html
    page-mobile.html
    page-android.html

The app will render the template with the lowest level possible. For example, for an iPhone user will look for templates in the following order:

    page-iphone.html
    page-ios.html
    page-mobile.html
    page-html

In this particular example, `page-mobile.html` would be rendered.
