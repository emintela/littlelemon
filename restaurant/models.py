from django.db import models


# Create your models here.
class Menu(models.Model):
    title = models.CharField(max_length=255, db_index=True, null=False, blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    inventory = models.SmallIntegerField(default=0, null=False, blank=False)
    
    def __str__(self):
        return f"{self.title}: {str(self.price)}"

    
class Booking(models.Model):
    name = models.CharField(max_length=255, db_index=True, null=False, blank=False)
    no_of_guests = models.SmallIntegerField(null=False, blank=False)
    booking_date = models.DateTimeField(db_index=True, null=False, blank=False)
    
    def __str__(self):
        return f"{self.name} for date: {str(self.booking_date)}"

class MenuItem(models.Model):
    # Your model fields and definitions here
    pass