# Generated by Django 2.2.9 on 2020-01-26 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0009_auto_20200126_1601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='telephone',
            field=models.CharField(max_length=30),
        ),
    ]
