# Generated by Django 4.1 on 2022-08-27 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0013_alter_teammembers_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teammembers',
            name='role',
            field=models.CharField(choices=[('1', 'kaptan'), ('2', 'yazılım'), ('3', 'mekanik'), ('4', 'elektronik')], default='4', max_length=2, verbose_name='takımdaki rolü'),
        ),
    ]
