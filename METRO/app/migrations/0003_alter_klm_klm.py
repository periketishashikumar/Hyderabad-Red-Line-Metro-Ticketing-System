# Generated by Django 5.1.3 on 2025-01-12 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_klm'),
    ]

    operations = [
        migrations.AlterField(
            model_name='klm',
            name='klm',
            field=models.FloatField(),
        ),
    ]
