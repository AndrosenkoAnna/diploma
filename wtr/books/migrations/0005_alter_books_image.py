# Generated by Django 3.2.8 on 2021-11-20 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_rename_book_books'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media', verbose_name='Изображение'),
        ),
    ]