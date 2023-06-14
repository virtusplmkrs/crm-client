# Generated by Django 4.2.2 on 2023-06-12 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_alter_customer_birth_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='area_code',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='customer',
            name='birth_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='cep',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
