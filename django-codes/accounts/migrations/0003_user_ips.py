# Generated by Django 4.2 on 2023-06-05 06:32

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_user_bio_alter_user_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='ips',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.GenericIPAddressField(), blank=True, null=True, size=None),
        ),
    ]
