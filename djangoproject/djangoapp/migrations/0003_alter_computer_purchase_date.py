# Generated by Django 4.1.1 on 2022-11-01 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0002_computer_purchase_date_computer_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computer',
            name='purchase_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
