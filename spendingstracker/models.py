from django.db import models

class Spending(models.Model):
    amount = models.IntegerField(default=1)
    currency = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    date = models.DateTimeField()

    def ___str___(self):
        return f"{self.date} {self.currency}{self.amount}"
