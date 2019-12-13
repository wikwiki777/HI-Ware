# Generated by Django 3.0 on 2019-12-06 18:35

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20191206_1730'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=30)),
                ('model', models.CharField(max_length=30)),
                ('description', models.TextField(max_length=500)),
                ('specifications', django.contrib.postgres.fields.jsonb.JSONField()),
                ('images', django.contrib.postgres.fields.jsonb.JSONField()),
                ('price', models.IntegerField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('baseproduct', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='products.BaseProduct')),
            ],
        ),
    ]