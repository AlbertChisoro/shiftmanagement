# Generated by Django 3.1.2 on 2020-10-19 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0008_auto_20201019_1255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeeshiftrecords',
            name='employee',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='employeeshiftrecords',
            name='shift',
            field=models.CharField(max_length=250),
        ),
    ]
