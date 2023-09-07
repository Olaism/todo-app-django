from django.http import Http404
from django.shortcuts import render

from .models import Category

def category_list(request):
    orderBy = request.GET.get('orderBy')
    if orderBy == 'created' or orderBy == '-created':
        categories = Category.objects.order_by(orderBy)
    elif orderBy == 'title' or orderBy == '-title':
        categories = Category.objects.order_by(orderBy)
    else:
        categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})
    
    
def category_detail(request, pk):
    try:
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        raise Http404('Category does not exists!')
    return render(request, 'category_detail.html', {'category': category})