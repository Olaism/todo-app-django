from django.urls import path

from .views import (
    category_list,
    category_detail
)

urlpatterns = [
    path('', category_list, name='category_list'),
    path('category/<int:pk>/', category_detail, name='category_detail'),
    # path('category/new/', category_new, name='category_new'),
    # path('category/<int:pk>/edit/', category_edit, name='category_edit'),
    # path('category/<int:pk>/delete/', category_delete, name='category_delete')
]