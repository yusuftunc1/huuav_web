# Generated by Django 4.1 on 2022-09-06 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0021_alter_managers_instagram_alter_managers_linkedin_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sponsors',
            name='level',
            field=models.CharField(choices=[('ANA', 'Ana'), ('ALTIN', 'Gold'), ('GÜMÜŞ', 'Silver')], max_length=10, verbose_name='Sponsorluk seviyesi'),
        ),
    ]
