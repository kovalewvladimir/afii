from django.shortcuts import render
from inventory import models
from django.http.response import HttpResponse
from django.db import connection


def main(request):
    args = {}
    args['title'] = 'test'

    pp = models.Printer.objects.select_related().prefetch_related('base_printer__base_cartridges__cartridges').all()
    #b = [c.shelf for p in pp for bc in p.base_printers.base_cartridges.all() for c in bc.cartridges.all()]

    args['printers'] = pp
    #args['space'] = models.Space.objects.all()

    return render(request, 'inventory/test.html', args)