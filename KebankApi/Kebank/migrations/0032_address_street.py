# Generated by Django 4.2.6 on 2023-11-09 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Kebank', '0031_user_email_alter_user_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='street',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
