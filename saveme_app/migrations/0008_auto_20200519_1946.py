# Generated by Django 2.2.4 on 2020-05-19 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saveme_app', '0007_community_community_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='missing',
            name='breed',
            field=models.CharField(default='', help_text='동물 품종', max_length=50),
        ),
    ]