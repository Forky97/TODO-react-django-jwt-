# Generated by Django 4.2.3 on 2023-07-16 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='done',
            field=models.BooleanField(default=False),
        ),
    ]
