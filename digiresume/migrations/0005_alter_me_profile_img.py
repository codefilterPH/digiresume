# Generated by Django 4.0.6 on 2022-09-01 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digiresume', '0004_rename_pro_img_me_profile_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='me',
            name='profile_img',
            field=models.ImageField(blank=True, null=True, upload_to='static/img/digiresume/media/me'),
        ),
    ]
