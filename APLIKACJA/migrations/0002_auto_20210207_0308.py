# Generated by Django 3.1.6 on 2021-02-07 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APLIKACJA', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='film',
            name='release_date',
            field=models.DateField(auto_now=True),
        ),
    ]