# Generated by Django 5.0.6 on 2024-06-19 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testdb', '0013_remove_post_test11'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='test11',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]