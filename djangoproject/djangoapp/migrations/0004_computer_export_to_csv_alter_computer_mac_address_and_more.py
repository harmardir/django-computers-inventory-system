# Generated by Django 4.1.1 on 2022-11-03 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0003_alter_computer_purchase_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='computer',
            name='export_to_CSV',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='computer',
            name='MAC_address',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='computer',
            name='computer_name',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='computer',
            name='ip_address',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='computer',
            name='location',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='computer',
            name='purchase_date',
            field=models.DateField(blank=True, null=True, verbose_name='Purchase date (mm/dd/yyyy)'),
        ),
        migrations.AlterField(
            model_name='computer',
            name='username',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
