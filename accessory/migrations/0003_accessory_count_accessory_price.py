# Generated by Django 4.1.7 on 2023-04-25 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accessory', '0002_alter_accessory_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='accessory',
            name='count',
            field=models.IntegerField(default=1, null=True),
        ),
        migrations.AddField(
            model_name='accessory',
            name='price',
            field=models.CharField(max_length=20, null=True),
        ),
    ]