# Generated by Django 4.1.2 on 2023-01-16 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('olx', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notifications',
            name='status',
            field=models.CharField(choices=[('cancelled', 'cancelled'), ('sent', 'sent'), ('pending', 'pending')], max_length=50),
        ),
    ]