# Generated by Django 3.2.15 on 2022-12-04 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_auto_20221203_2208'),
    ]

    operations = [
        migrations.AddField(
            model_name='userauth',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
