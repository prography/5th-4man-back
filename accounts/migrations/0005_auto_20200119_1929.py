# Generated by Django 2.2.6 on 2020-01-19 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20200118_1743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='upload_image',
            field=models.ImageField(blank=True, default='default_user_image.png', upload_to='user_image/profile/%Y/%m/%d/', verbose_name='프로필 사진'),
        ),
    ]
