# Generated by Django 5.1.3 on 2024-11-28 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bands', '0004_alter_band_options_alter_musician_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='venue',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='venue',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
