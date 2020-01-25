# Generated by Django 2.2.7 on 2020-01-25 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfileInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctorName', models.CharField(max_length=200)),
                ('doctorId', models.CharField(max_length=200, unique=True)),
                ('hospitalName', models.CharField(max_length=200)),
                ('profile_pic', models.ImageField(blank=True, upload_to='profile_pics')),
            ],
        ),
    ]