from django import forms

from .models import Budget, Category


class BudgetSelectForm(forms.ModelForm):
    budget = forms.ModelChoiceField(queryset=Budget.objects.all())

    class Meta:
        model = Category
        fields = ('budget',)