# Generated by Django 4.0.6 on 2022-07-10 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='bio',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='artist',
            name='dateofbirth',
            field=models.DateField(blank=True, null=True),
        ),
    ]
