# Generated by Django 5.0.6 on 2024-06-14 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a_home', '0002_withoutborders'),
    ]

    operations = [
        migrations.AddField(
            model_name='withoutborders',
            name='days',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]