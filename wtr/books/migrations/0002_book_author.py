# Generated by Django 3.2.8 on 2021-11-10 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.CharField(default='Неизвестен', max_length=100),
        ),
    ]
