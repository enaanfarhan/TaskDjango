# Generated by Django 3.0.7 on 2020-07-01 19:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_studentdetail'),
    ]

    operations = [
        migrations.DeleteModel(
            name='StudentDetails',
        ),
    ]