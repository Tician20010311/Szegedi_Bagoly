# Generated by Django 5.0.6 on 2024-06-14 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a_home', '0004_remove_withoutborders_image_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Firstday',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images')),
            ],
        ),
    ]
