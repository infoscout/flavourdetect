from flavourdetect.utils import flavour_detect

class FlavourDetectMiddleware(object):

    def process_request(self, request):
        request.flavour = flavour_detect(request)
        