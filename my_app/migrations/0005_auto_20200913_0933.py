# Generated by Django 3.1.1 on 2020-09-13 12:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0004_venda'),
    ]

    operations = [
        migrations.RenameField(
            model_name='venda',
            old_name='fornecedor',
            new_name='comprador',
        ),
    ]