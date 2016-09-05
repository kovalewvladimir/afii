from django.shortcuts import render
from inventory import models
from django.http.response import HttpResponse

def main(request):
    args = {}
    args['title'] = 'test'
    # s = models.Space.objects.all()
    # s0 = s[0]
    # st = models.Storage.objects.get(pk=s0.id)

    return render(request, 'inventory/test.html', args)
