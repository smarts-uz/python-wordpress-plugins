# Generated by Django 5.0.4 on 2024-04-23 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Plugin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=255)),
                ('url', models.CharField(max_length=255)),
                ('folder_path', models.CharField(blank=True, max_length=255, null=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('zipfile', models.CharField(blank=True, max_length=255, null=True)),
                ('screenshot', models.BooleanField(default=False)),
                ('elements', models.BooleanField(default=False)),
                ('html', models.CharField(blank=True, max_length=255, null=True)),
                ('owner_name', models.CharField(blank=True, max_length=255, null=True)),
                ('unused', models.BooleanField(default=False)),
                ('fivestars', models.IntegerField(blank=True, null=True)),
                ('last_updated', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'plugin',
                'managed': False,
            },
        ),
    ]
