# Generated by Django 2.1.5 on 2019-01-15 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mailroom', '0007_retrieve'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='Status',
            field=models.BooleanField(default=False),
        ),
    ]
