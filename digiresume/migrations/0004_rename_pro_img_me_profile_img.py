# Generated by Django 4.0.6 on 2022-09-01 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('digiresume', '0003_me_pro_img'),
    ]

    operations = [
        migrations.RenameField(
            model_name='me',
            old_name='pro_img',
            new_name='profile_img',
        ),
    ]
