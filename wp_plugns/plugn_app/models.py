from django.db import models


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class Plugin(models.Model):
    id = models.AutoField(primary_key=True)
    slug = models.CharField(max_length=255, unique=True)
    url = models.URLField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    zipfile = models.CharField(max_length=255, blank=True, null=True)
    screenshot = models.BooleanField(default=False)
    elements = models.BooleanField(default=False)
    html = models.CharField(max_length=255, blank=True, null=True)
    owner_name = models.CharField(max_length=255, blank=True, null=True)
    unused = models.BooleanField(default=False)
    fivestars = models.IntegerField(blank=True, null=True)
    last_updated = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'plugin'  # Keep the table name
        ordering = ['name']
        verbose_name = "Plugin"
        verbose_name_plural = "Plugins"

    def __str__(self):
        return self.name or f"Plugin {self.slug}"