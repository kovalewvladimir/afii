from django.shortcuts import render
from inventory import models
from django.http.response import HttpResponse
from django.db import connection


def main(request):


    args = {}
    args['title'] = 'test'

    #args['printer'] = models.Printer.objects.select_related().all()
    args['space'] = models.Space.objects.all()

    p = models.Printer.objects.all()


    return render(request, 'inventory/test.html', args)