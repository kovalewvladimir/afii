from django.shortcuts import render
from django.http.response import HttpResponse

def main(request):
    args = {}
    args['title'] = 'test'
    return render(request, 'inventory/test.html', args)
