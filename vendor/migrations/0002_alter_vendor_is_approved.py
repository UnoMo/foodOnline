# Generated by Django 4.2.6 on 2023-10-21 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='is_approved',
            field=models.BooleanField(default=False),
        ),
    ]
