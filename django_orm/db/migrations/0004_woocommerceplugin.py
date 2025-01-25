# Generated by Django 4.2.18 on 2025-01-25 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0003_plugin_delete_plugin_wr'),
    ]

    operations = [
        migrations.CreateModel(
            name='WooCommercePlugin',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('slug', models.CharField(max_length=255, unique=True)),
                ('url', models.URLField(blank=True, max_length=2000)),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('zipfile', models.FileField(blank=True, null=True, upload_to='woocommerce/plugins/zipfiles/')),
                ('screenshot', models.URLField(blank=True, null=True)),
                ('elements', models.JSONField(blank=True, null=True)),
                ('html', models.TextField(blank=True, null=True)),
                ('owner_name', models.CharField(blank=True, max_length=255, null=True)),
                ('unused', models.BooleanField(default=False)),
                ('fivestars', models.DecimalField(blank=True, decimal_places=1, max_digits=2, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
