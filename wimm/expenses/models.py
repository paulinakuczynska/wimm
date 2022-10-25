from django.db import models

class Budget(models.Model):
    budget_name = models.CharField(max_length=20, null=False)
    income = models.DecimalField(default=0, max_digits=8, decimal_places=2, null=False)

    def __str__(self) -> str:
        return self.budget_name

class Category(models.Model):
    category_name = models.CharField(max_length=20, null=False)
    limit = models.DecimalField(max_digits=8, decimal_places=2, null=False)
    spent = models.DecimalField(default=0, max_digits=8, decimal_places=2, null=False)
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE, null=False)

    def __str__(self) -> str:
        return f'{self.category_name}'