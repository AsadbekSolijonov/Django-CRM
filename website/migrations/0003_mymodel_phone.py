# Generated by Django 4.2.5 on 2024-06-18 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_mymodel_odd_filed'),
    ]

    operations = [
        migrations.AddField(
            model_name='mymodel',
            name='phone',
            field=models.CharField(default=1, max_length=11),
            preserve_default=False,
        ),
    ]
