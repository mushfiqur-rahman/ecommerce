# Generated by Django 4.2.3 on 2023-12-17 15:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_alter_order_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'ordering': ['user__first_name', 'user__last_name'], 'permissions': [('view_history', 'Can view history')]},
        ),
    ]
