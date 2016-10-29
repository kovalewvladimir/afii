from django.shortcuts import render, get_object_or_404
from storage import models


def storage_view(request, storage_id):
    storage = get_object_or_404(models.Storage, pk=int(storage_id))
    space = storage.space

    args = {
        'space': space,
        'storage': storage,
    }

    return render(request, 'space/base.html', args)
