# Generated by Django 4.2.4 on 2023-08-11 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='img',
            field=models.ImageField(default='ddffgg', upload_to='gallery'),
            preserve_default=False,
        ),
    ]
