from django.db import models

class ExpenseCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Transaction(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(ExpenseCategory, on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateField()
    comments = models.TextField(blank=True)

class Budget(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    allocated_amount = models.DecimalField(max_digits=10, decimal_places=2)

class AIModel(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    model_file = models.FileField(upload_to='ai_models/')
