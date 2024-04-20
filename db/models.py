# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Plugin(models.Model):
    slug = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    zipfile = models.BooleanField(default=False)
    screenshot = models.BooleanField(default=False)
    elements = models.BooleanField(default=False)
    demo = models.CharField(max_length=255, default=False)
    html = models.BooleanField(default=False)




    def _str_(self):
        return self.slug

