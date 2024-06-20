# Generated by Django 4.2.5 on 2024-06-18 04:56

from django.db import migrations, models
import website.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('even_field', models.IntegerField(validators=[website.validators.even_number_validate])),
            ],
        ),
    ]