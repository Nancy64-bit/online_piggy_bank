from django.db import models

class PiggyBank(models.Model):
    is_broken = models.BooleanField(default=False)

class Transaction(models.Model):
    piggy_bank = models.ForeignKey(PiggyBank, on_delete=models.CASCADE, null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
