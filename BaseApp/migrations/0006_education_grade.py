# Generated by Django 3.1.4 on 2021-01-20 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BaseApp', '0005_certificate_education'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='grade',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=3),
            preserve_default=False,
        ),
    ]
