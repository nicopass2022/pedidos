# Generated by Django 4.0.4 on 2022-04-26 23:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0018_rename_avarat_avatar'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlbumImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images')),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='AppCoder.articulos')),
            ],
        ),
    ]
