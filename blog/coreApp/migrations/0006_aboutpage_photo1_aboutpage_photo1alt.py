# Generated by Django 5.0.2 on 2024-02-19 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coreApp', '0005_aboutpage'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutpage',
            name='photo1',
            field=models.ImageField(default='about_photos/LOGO.jpg', upload_to='about_photos/'),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='photo1alt',
            field=models.CharField(default='about img', max_length=200),
        ),
    ]
