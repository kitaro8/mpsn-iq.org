# Generated by Django 5.0.6 on 2024-06-20 00:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testdb', '0015_post_file3_post_image2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='test11',
        ),
    ]