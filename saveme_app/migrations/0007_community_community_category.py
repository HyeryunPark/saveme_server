# Generated by Django 2.2.4 on 2020-05-14 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saveme_app', '0006_auto_20200508_1457'),
    ]

    operations = [
        migrations.AddField(
            model_name='community',
            name='community_category',
            field=models.CharField(default='', help_text='글 카테고리', max_length=20),
        ),
    ]
