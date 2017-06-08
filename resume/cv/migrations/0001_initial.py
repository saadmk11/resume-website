# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('institute_name', models.CharField(max_length=50)),
                ('subject', models.CharField(max_length=40)),
                ('year', models.DateField(null=True, blank=True)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='PersonalInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('birth_day', models.DateField()),
                ('gender', models.CharField(max_length=6, choices=[(b'Male', b'Male'), (b'Female', b'Female')])),
                ('nationality', models.CharField(max_length=25)),
                ('phone_no', models.CharField(max_length=14, blank=True)),
                ('email', models.EmailField(max_length=254)),
                ('website', models.URLField(blank=True)),
                ('address', models.CharField(max_length=100, blank=True)),
                ('bio', models.TextField()),
                ('picture', models.ImageField(height_field=b'height_field', width_field=b'width_field', null=True, upload_to=b'', blank=True)),
                ('height_field', models.IntegerField(default=600)),
                ('width_field', models.IntegerField(default=600)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('language_skills', models.CharField(help_text=b'Sparate languages by comma', max_length=200, blank=True)),
                ('other_skills', models.CharField(help_text=b'Sparate Skills by comma', max_length=200, blank=True)),
                ('personal_info', models.ForeignKey(to='cv.PersonalInfo')),
            ],
        ),
        migrations.CreateModel(
            name='WorkExperience',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('company_name', models.CharField(max_length=50)),
                ('job_title', models.CharField(max_length=20)),
                ('joining_year', models.DateField(null=True, blank=True)),
                ('job_description', models.TextField()),
                ('personal_info', models.ForeignKey(to='cv.PersonalInfo')),
            ],
        ),
        migrations.AddField(
            model_name='education',
            name='personal_info',
            field=models.ForeignKey(to='cv.PersonalInfo'),
        ),
    ]
