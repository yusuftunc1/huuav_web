# Generated by Django 4.1 on 2022-08-27 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0014_alter_teammembers_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teammembers',
            name='role',
            field=models.CharField(choices=[('kaptan', 'Cap'), ('yazılım', 'Sof'), ('mekanik', 'Mec'), ('elektronik', 'Ele')], default='elektronik', max_length=10, verbose_name='takımdaki rolü'),
        ),
    ]