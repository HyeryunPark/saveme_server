# Generated by Django 2.2.4 on 2020-04-04 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Missing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(default='', help_text='실종상태입력 (실종,보호,목격,완료)', max_length=3)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('city', models.CharField(default='', help_text='시', max_length=10)),
                ('district', models.CharField(default='', help_text='구', max_length=10)),
                ('detailLocation', models.CharField(default='', help_text='상세주소', max_length=30)),
                ('phone', models.CharField(default='', help_text='작성자 핸드폰번호', max_length=11)),
                ('species', models.CharField(default='', help_text='동물 종', max_length=5)),
                ('breed', models.CharField(default='', help_text='동물 품종', max_length=20)),
                ('gender', models.CharField(default='', help_text='성별', max_length=3)),
                ('neuter', models.BooleanField(default=False, help_text='중성화여부')),
                ('age', models.CharField(default='', help_text='나이', max_length=5)),
                ('weight', models.CharField(default='', help_text='몸무게', max_length=10)),
                ('pattern', models.CharField(default='', help_text='털 색', max_length=10)),
                ('feature', models.CharField(default='', help_text='특징', max_length=30)),
                ('etc', models.CharField(default='', help_text='기타', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Shelter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(default='', help_text='공고상태입력', max_length=3)),
                ('species', models.CharField(default='', help_text='종', max_length=5)),
                ('breed', models.CharField(default='', help_text='품종', max_length=20)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('area', models.CharField(default='', help_text='지역', max_length=20)),
                ('spot', models.CharField(default='', help_text='발견 장소', max_length=30)),
                ('gender', models.CharField(default='', help_text='성별', max_length=3)),
                ('neuter', models.BooleanField(default=False, help_text='중성화 여부')),
                ('pattern', models.CharField(default='', help_text='털 색', max_length=10)),
                ('age', models.CharField(default='', help_text='나이', max_length=10)),
                ('weight', models.CharField(default='', help_text='몸무게', max_length=5)),
                ('notice_number', models.CharField(default='', help_text='공고번호', max_length=20)),
                ('feature', models.CharField(default='', help_text='특이사항', max_length=30)),
                ('protection_center', models.CharField(default='', help_text='보호센터', max_length=20)),
                ('department_in_charge', models.CharField(default='', help_text='담당부서', max_length=20)),
                ('protection_center_phone', models.CharField(default='', help_text='보호센터 전화번호', max_length=11)),
                ('protection_center_address', models.CharField(default='', help_text='보호센터 주소', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userEmail', models.CharField(default='', max_length=25, unique=True)),
                ('userPw', models.CharField(default='', max_length=25)),
            ],
        ),
    ]
