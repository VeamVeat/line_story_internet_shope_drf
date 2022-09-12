# Generated by Django 4.1 on 2022-09-12 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('countries', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='name',
            field=models.CharField(max_length=255, verbose_name='country'),
        ),
        migrations.AlterField(
            model_name='country',
            name='reduction',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='reduction'),
        ),
    ]