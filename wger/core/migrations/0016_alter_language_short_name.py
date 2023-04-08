# Generated by Django 4.2 on 2023-04-07 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_alter_language_short_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='language',
            name='short_name',
            field=models.CharField(
                help_text='ISO 639-1',
                max_length=2,
                unique=True,
                verbose_name='Language short name'
            ),
        ),
    ]
