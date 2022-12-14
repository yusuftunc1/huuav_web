# Generated by Django 4.1 on 2022-08-26 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_teams'),
    ]

    operations = [
        migrations.CreateModel(
            name='teammembers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('1', 'kaptan'), ('2', 'yazılım'), ('3', 'mekanik'), ('4', 'elektronik')], default='4', max_length=2)),
                ('teamname', models.CharField(max_length=50, verbose_name='takım adı')),
                ('name', models.CharField(max_length=50, verbose_name='İsim')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('linkedin', models.TextField(verbose_name='email')),
            ],
        ),
    ]
