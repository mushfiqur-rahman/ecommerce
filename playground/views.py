from django.shortcuts import render
from store.models import Product


def say_hello(request):
    queryset = Product.objects.prefetch_related('collection').all()

    return render(request, 'index.html', {'name': 'Mushfiq', 'products': list(queryset)})
