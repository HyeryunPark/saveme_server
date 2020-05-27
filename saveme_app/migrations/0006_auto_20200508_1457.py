# Generated by Django 2.2.4 on 2020-05-08 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saveme_app', '0005_auto_20200507_2022'),
    ]

    operations = [
        migrations.AddField(
            model_name='community',
            name='user_name',
            field=models.CharField(default='', help_text='작성자 이름', max_length=10),
        ),
        migrations.AlterField(
            model_name='community',
            name='community_date',
            field=models.DateTimeField(auto_now_add=True, help_text='작성한 날짜'),
        ),
    ]
