# Generated by Django 4.0.6 on 2022-07-27 03:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0011_alter_transactions_serial_number_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Transactions',
            new_name='Transaction',
        ),
    ]
