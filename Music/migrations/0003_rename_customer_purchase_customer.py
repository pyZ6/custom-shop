# Generated by Django 4.1.7 on 2023-04-12 12:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Music', '0002_customer_item_purchase_delete_album_delete_musician_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='purchase',
            old_name='Customer',
            new_name='customer',
        ),
    ]
