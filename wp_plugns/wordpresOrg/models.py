from django.db import models
from django.utils import timezone

class wordpres_org(models.Model):
    slug = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    zipfile = models.URLField(null=True, blank=True)
    screenshot = models.URLField(null=True, blank=True)
    fivestars = models.FloatField(null=True, blank=True)
    last_updated = models.DateTimeField(null=True, blank=True)
    tested = models.CharField(max_length=255, null=True, blank=True)
    requires = models.CharField(max_length=255, null=True, blank=True)
    ratings = models.IntegerField(null=True, blank=True)
    downloaded = models.IntegerField(null=True, blank=True)
    tags = models.JSONField(null=True, blank=True)

    def __str__(self):
        return self.name or self.slug

    def save(self, *args, **kwargs):
        if self.last_updated is None:
            self.last_updated = timezone.now()
        super().save(*args, **kwargs)