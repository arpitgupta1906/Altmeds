# Generated by Django 2.2.7 on 2020-01-25 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20200125_2047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='isApproved',
            field=models.IntegerField(default=0),
        ),
    ]