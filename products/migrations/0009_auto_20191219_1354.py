# Generated by Django 3.0 on 2019-12-19 13:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20191218_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baseproduct',
            name='category',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='products.Category'),
        ),
    ]
