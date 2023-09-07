from django.http import Http404
from django.shortcuts import render

from .models import Category

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})
    
    
def category_detail(request, pk):
    try:
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        raise Http404('Category does not exists!')
    return render(request, 'category_detail.html', {'category': category})