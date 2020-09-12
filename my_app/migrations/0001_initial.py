# Generated by Django 3.1.1 on 2020-09-12 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fornecedor', models.CharField(max_length=30)),
                ('produto', models.CharField(max_length=30)),
                ('cor', models.CharField(max_length=30)),
                ('marca', models.CharField(max_length=30)),
                ('tamanho', models.CharField(max_length=10)),
                ('valor', models.FloatField()),
                ('data_recebimento', models.DateField()),
            ],
        ),
    ]