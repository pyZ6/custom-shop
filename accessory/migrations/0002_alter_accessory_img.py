# Generated by Django 4.1.7 on 2023-04-23 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accessory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accessory',
            name='img',
            field=models.ImageField(null=True, upload_to='Accessory_images'),
        ),
    ]
