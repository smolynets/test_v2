from django.shortcuts import render

from django.http import HttpResponse


def list(request):
    return render(request, 'mytest/list.html', {})

def one_test(request, test_id):
    return render(request, 'mytest/one_test.html', {'tt': test_id})