# Generated by Django 3.1.1 on 2020-09-13 02:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0002_pessoa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='fornecedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='my_app.pessoa'),
        ),
    ]
