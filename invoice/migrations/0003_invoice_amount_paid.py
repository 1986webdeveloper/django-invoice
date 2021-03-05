# Generated by Django 3.1.7 on 2021-03-04 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0002_invoice_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='amount_paid',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True),
        ),
    ]