# Generated by Django 2.2.9 on 2020-02-04 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0012_logger'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logger',
            name='method',
            field=models.CharField(max_length=10),
        ),
    ]
