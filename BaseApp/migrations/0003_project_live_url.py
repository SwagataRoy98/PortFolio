# Generated by Django 3.1.4 on 2021-01-17 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BaseApp', '0002_auto_20210117_1800'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='live_url',
            field=models.CharField(default='Not Applicable', max_length=250),
            preserve_default=False,
        ),
    ]
