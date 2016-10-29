from space.models import Space


def spaces(request):
    return {'spaces': Space.objects.all()}
