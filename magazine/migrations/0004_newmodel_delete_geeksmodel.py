# Generated by Django 4.1.7 on 2023-04-11 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0003_geeksmodel_delete_example'),
    ]

    operations = [
        migrations.CreateModel(
            name='newModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='GeeksModel',
        ),
    ]