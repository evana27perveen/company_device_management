# Generated by Django 4.2 on 2023-04-05 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='user',
        ),
        migrations.AddField(
            model_name='employee',
            name='name',
            field=models.CharField(default='Null', max_length=100),
            preserve_default=False,
        ),
    ]