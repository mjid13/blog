# Generated by Django 5.0.2 on 2024-02-18 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coreApp', '0003_indexpage_slag'),
    ]

    operations = [
        migrations.AddField(
            model_name='indexpage',
            name='supslag',
            field=models.CharField(default='أبداء رحلتك بالتعلم العميق و المفيد بتصفح احدى مقالتنا', max_length=500),
        ),
    ]
