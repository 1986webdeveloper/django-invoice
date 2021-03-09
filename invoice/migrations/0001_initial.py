# Generated by Django 3.1.7 on 2021-03-09 04:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_logo', models.ImageField(blank=True, null=True, upload_to='images/invoice_img')),
                ('invoice_num', models.CharField(blank=True, max_length=100, null=True)),
                ('invoice_date', models.DateField(blank=True, null=True)),
                ('due_date', models.DateField(blank=True, null=True)),
                ('invoice_from', models.CharField(blank=True, max_length=100, null=True)),
                ('notes', models.CharField(blank=True, max_length=100, null=True)),
                ('payment_terms', models.CharField(blank=True, max_length=100, null=True)),
                ('terms_and_conditions', models.CharField(blank=True, max_length=100, null=True)),
                ('billing_address', models.CharField(blank=True, max_length=200, null=True)),
                ('shipping_address', models.CharField(blank=True, max_length=200, null=True)),
                ('total', models.DecimalField(blank=True, decimal_places=3, max_digits=20, null=True)),
                ('discount', models.DecimalField(blank=True, decimal_places=3, max_digits=20, null=True)),
                ('shipping_charge', models.DecimalField(blank=True, decimal_places=3, max_digits=20, null=True)),
                ('tax', models.DecimalField(blank=True, decimal_places=3, max_digits=20, null=True)),
                ('balance_due', models.DecimalField(blank=True, decimal_places=3, max_digits=20, null=True)),
                ('subtotal', models.DecimalField(blank=True, decimal_places=3, max_digits=20, null=True)),
                ('amount_paid', models.DecimalField(blank=True, decimal_places=3, max_digits=20, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='users', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='InvoiceLine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(blank=True, max_length=150, null=True)),
                ('item_description', models.CharField(blank=True, max_length=200, null=True)),
                ('quantity', models.IntegerField(default=1)),
                ('price', models.DecimalField(blank=True, decimal_places=3, max_digits=20, null=True)),
                ('line_total', models.DecimalField(blank=True, decimal_places=3, max_digits=20, null=True)),
                ('invoice', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='invoice.invoice')),
            ],
        ),
    ]
