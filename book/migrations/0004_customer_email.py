# Generated by Django 4.1 on 2022-09-02 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_alter_book_table_alter_cart_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='email',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
