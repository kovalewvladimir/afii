from django.shortcuts import render
from inventory import models
from django.http.response import HttpResponse
from django.db import connection


def main(request):
    args = {}
    args['title'] = 'test'

    pp = models.Printer.objects.select_related().prefetch_related('base_printer__base_cartridges__cartridges').all()

    return render(request, 'inventory/test.html', args)