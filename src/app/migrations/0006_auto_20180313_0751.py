# Generated by Django 2.0.3 on 2018-03-13 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_service_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='short_url',
            field=models.CharField(blank=True, max_length=200, null=True, unique=True),
        ),
    ]
