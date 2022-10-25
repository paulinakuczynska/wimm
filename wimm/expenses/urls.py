from django.urls import path, reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

from .models import Category
from .views import CategoryListView

urlpatterns = [
    path('', CategoryListView.as_view(), name='expenses'),
    path('<int:pk>/edit/',
        UpdateView.as_view(
            model=Category,
            fields=('category_name', 'limit', 'spent'),
            success_url=reverse_lazy('expenses'),
            template_name='generic_update.html'
        ),
        name='expenses-edit'),
    path('<int:pk>/delete/',
        DeleteView.as_view(
            model=Category,
            success_url=reverse_lazy('expenses'),
            template_name='generic_delete.html'
        ),
        name='expenses-delete'),
]