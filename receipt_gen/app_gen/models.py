from django.db import models

class Receipt(models.Model):
    receipt_number = models.CharField(max_length=100)
    date = models.DateField()
    received_from = models.CharField(max_length=255)
    sum_amount = models.DecimalField(max_digits=10, decimal_places=2)
    actual_amount = models.DecimalField(max_digits=10, decimal_places=2)
    signature = models.CharField(max_length=255)
    payment_details = models.TextField()
    payment_method = models.CharField(max_length=100)

    def __str__(self):
        return self.receipt_number
