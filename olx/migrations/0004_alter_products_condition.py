# Generated by Django 4.1.2 on 2023-01-18 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('olx', '0003_alter_notifications_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='condition',
            field=models.CharField(choices=[('New', 'New'), ('Used', 'Used')], max_length=200),
        ),
    ]
