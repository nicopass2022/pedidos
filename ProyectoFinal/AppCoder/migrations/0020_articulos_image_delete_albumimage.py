# Generated by Django 4.0.4 on 2022-04-27 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0019_albumimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='articulos',
            name='image',
            field=models.ImageField(blank=True, default='images/engranaje.jpg', null=True, upload_to='images'),
        ),
        migrations.DeleteModel(
            name='AlbumImage',
        ),
    ]
