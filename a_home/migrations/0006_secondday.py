# Generated by Django 5.0.6 on 2024-06-14 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a_home', '0005_firstday'),
    ]

    operations = [
        migrations.CreateModel(
            name='Secondday',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images')),
            ],
        ),
    ]
