from django.urls import path, reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

from .models import Category, Budget
from .views import CategoryListView

urlpatterns = [
    path('', CategoryListView.as_view(), name='expenses'),
    path('expenses/create/',
        CreateView.as_view(
            model=Category,
            fields='__all__',
            success_url=reverse_lazy('expenses'),
            template_name='generic_update.html'
        ),
        name='expenses-create'),
    path('<int:pk>/spent/',
        UpdateView.as_view(
            model=Category,
            fields=('spent',),
            success_url=reverse_lazy('expenses'),
            template_name='generic_update.html'
        ),
        name='expenses-spent'),
    path('<int:pk>/edit/',
        UpdateView.as_view(
            model=Category,
            fields=('category_name', 'limit'),
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
    path('expenses/create/budget',
        CreateView.as_view(
            model=Budget,
            fields='__all__',
            success_url=reverse_lazy('expenses'),
            template_name='generic_update.html'
        ),
        name='expenses-create-budget'),
    path('<int:pk>/edit/budget',
        UpdateView.as_view(
            model=Budget,
            fields='__all__',
            success_url=reverse_lazy('expenses'),
            template_name='generic_update.html'
        ),
        name='expenses-edit-budget'),
    path('<int:pk>/delete/budget',
        DeleteView.as_view(
            model=Budget,
            success_url=reverse_lazy('expenses'),
            template_name='generic_delete.html'
        ),
        name='expenses-delete-budget'),
]