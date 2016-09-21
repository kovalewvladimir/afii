from inventory.models import Space


def space(request):
    return {'space': Space.objects.all()}