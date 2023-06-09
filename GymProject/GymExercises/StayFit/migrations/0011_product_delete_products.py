# Generated by Django 4.1.7 on 2023-04-04 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StayFit', '0010_alter_products_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('image', models.ImageField(upload_to='media/')),
            ],
        ),
        migrations.DeleteModel(
            name='Products',
        ),
    ]
