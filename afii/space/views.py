from django.shortcuts import render, get_object_or_404
from space import models


def space_view(request, space_id):
    space = get_object_or_404(models.Space, pk=int(space_id))

    args = {
        'space': space,
    }

    return render(request, 'space/base.html', args)
