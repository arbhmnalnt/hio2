# Generated by Django 4.2.3 on 2023-10-05 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0003_userayada'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userayada',
            name='count',
            field=models.IntegerField(),
        ),
    ]