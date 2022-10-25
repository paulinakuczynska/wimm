from django.views.generic.list import ListView
from django.db.models import Sum

from .models import Budget, Category
from .forms import BudgetSelectForm


class CategoryListView(ListView):
    model = Category

    def get_context_data(self, **kwargs):
        queryset = self.object_list
        display_budget = Budget.objects.last()

        form = BudgetSelectForm(self.request.GET)
        if form.is_valid():
            selected_budget = form.cleaned_data.get('budget')
            if selected_budget:
                display_budget = selected_budget
                queryset = queryset.filter(budget=display_budget)
        else:
            queryset = queryset.filter(budget=display_budget)
        
        total_limit = queryset.aggregate(sum=Sum('limit'))['sum']
        total_spent = queryset.aggregate(sum=Sum('spent'))['sum']

        return super().get_context_data(
            form=form,
            object_list=queryset,
            total_limit=total_limit,
            total_spent=total_spent,
            display_budget=display_budget,
            **kwargs
        )