# Generated by Django 4.0.3 on 2022-03-16 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_rename_modigy_date_post_modify_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='blog/images/%Y/%m/%d/'),
        ),
    ]
