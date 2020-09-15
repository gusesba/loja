# Generated by Django 3.1.1 on 2020-09-14 20:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0005_auto_20200913_0933'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venda',
            name='id',
        ),
        migrations.AlterField(
            model_name='venda',
            name='produto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, primary_key=True, serialize=False, to='my_app.produto'),
        ),
    ]