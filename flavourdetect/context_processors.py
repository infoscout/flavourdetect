from flavourdetect.utils import all_flavours


def flavour(request):
    return {
        'flavour': request.flavour,
        'flavours': all_flavours(request.flavour),
    }
