from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from space import models


@login_required
def space_view(request, space_id):
    """
    Простая функция для отображения шаблона space/base.html.
    На данный момент нигде не используются, в дальнейшем можно удалить.
    :param request: http запрос
    :param space_id: id плащадки
    :return: http ответ
    """
    space = get_object_or_404(models.Space, pk=int(space_id))

    args = {
        'space': space,
    }

    return render(request, 'space/base.html', args)
