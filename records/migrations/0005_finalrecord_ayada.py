# Generated by Django 4.2.3 on 2023-10-05 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0004_alter_userayada_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='finalrecord',
            name='ayada',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='اسم العيادة'),
        ),
    ]
