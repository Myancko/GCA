# Generated by Django 4.1.5 on 2023-01-28 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0003_customuser_primeiro_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='primeiro_login',
            field=models.BooleanField(default=True),
        ),
    ]
