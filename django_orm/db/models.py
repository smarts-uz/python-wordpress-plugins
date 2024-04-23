# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Plugin(models.Model):
    slug = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    folder_path = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    zipfile = models.CharField(max_length=255, blank=True, null=True)
    screenshot = models.BooleanField()
    elements = models.BooleanField()
    demo = models.CharField(max_length=255)
    html = models.CharField(max_length=255, blank=True, null=True)
    owner_name = models.CharField(max_length=255,blank=True, null=True)
    unused = models.BooleanField(blank=True, null=True)
    fivestars = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'plugin'
