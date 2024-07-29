# Generated by Django 5.0.7 on 2024-07-28 19:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_category_category_name_alter_category_slug_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colorvariant',
            name='color_name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='static/products'),
        ),
        migrations.AlterField(
            model_name='quantityvariant',
            name='variant_name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='sizevariant',
            name='size_name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='static/products')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='home.product')),
            ],
        ),
    ]