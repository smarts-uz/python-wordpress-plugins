from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    link = models.URLField(max_length=200)
    vendor_name = models.CharField(max_length=255)
    description = models.TextField()
    rating = models.FloatField(null=True, blank=True)  # Rating optional bo'lishi mumkin
    reviews = models.IntegerField(null=True, blank=True)  # Agar mavjud bo'lsa, bu maydonni saqlash
    price = models.CharField(max_length=255)  # Agar narx har doim matn bo'lsa
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name