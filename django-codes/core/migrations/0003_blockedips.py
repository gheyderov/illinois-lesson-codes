# Generated by Django 4.2 on 2023-06-05 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_contact_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlockedIps',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.GenericIPAddressField()),
            ],
        ),
    ]
