# Generated by Django 4.1.4 on 2023-04-27 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0012_alter_settings_background_image_alter_settings_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settings',
            name='background_image',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='settings',
            name='logo',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
