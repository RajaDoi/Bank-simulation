from django.db import models

# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    aadhar_no = models.CharField(max_length=12, unique=True)
    phone = models.CharField(max_length=10)
    customer_ID = models.PositiveIntegerField(unique=True)

    def save(self, *args, **kwargs):
        if not self.customer_ID:
            last_customer = Customer.objects.order_by('-customer_ID').first()
            self.customer_ID = 8000 if not last_customer else last_customer.customer_ID + 1
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

