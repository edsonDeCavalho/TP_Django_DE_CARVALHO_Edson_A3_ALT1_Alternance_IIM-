# Generated by Django 4.0.2 on 2022-03-01 13:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_remove_product_views_profile_views'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='views',
            new_name='number',
        ),
    ]
