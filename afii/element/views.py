from django.shortcuts import render


def paper_view(request, paper_id):

    args = {}

    return render(request, 'element/base.html', args)
