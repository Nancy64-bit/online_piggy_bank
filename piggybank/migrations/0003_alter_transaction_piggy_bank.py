# Generated by Django 4.2.6 on 2023-10-11 05:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('piggybank', '0002_remove_piggybank_transactions_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='piggy_bank',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='piggybank.piggybank'),
        ),
    ]
