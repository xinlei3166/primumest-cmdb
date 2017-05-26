# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-25 14:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CpuUse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.CharField(max_length=32, verbose_name=b'cpu\xe4\xbd\xbf\xe7\x94\xa8\xe7\x8e\x87')),
                ('time', models.CharField(max_length=32, verbose_name=b'\xe6\x97\xb6\xe9\x97\xb4')),
            ],
            options={
                'verbose_name': 'CPU',
                'verbose_name_plural': 'CPU',
            },
        ),
        migrations.CreateModel(
            name='Departments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name=b'\xe9\x83\xa8\xe9\x97\xa8\xe5\x90\x8d\xe7\xa7\xb0')),
                ('description', models.TextField(max_length=500, verbose_name=b'\xe9\x83\xa8\xe9\x97\xa8\xe6\x8f\x8f\xe8\xbf\xb0')),
            ],
            options={
                'verbose_name': '\u90e8\u95e8',
                'verbose_name_plural': '\u90e8\u95e8',
            },
        ),
        migrations.CreateModel(
            name='GroupProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name=b'\xe7\xbb\x84\xe5\x90\x8d')),
                ('description', models.TextField(max_length=500, verbose_name=b'\xe7\xbb\x84\xe6\x8f\x8f\xe8\xbf\xb0')),
            ],
            options={
                'verbose_name': '\u7ec4',
                'verbose_name_plural': '\u7ec4',
            },
        ),
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name=b'\xe5\x8f\xaf\xe7\x94\xa8\xe6\x9d\x83\xe9\x99\x90')),
                ('codename', models.CharField(max_length=64)),
                ('content_type_id', models.IntegerField(help_text=b'\xe5\x90\x8c\xe4\xb8\x80\xe8\xa7\x92\xe8\x89\xb2\xe4\xb8\x8b\xe7\x9a\x84\xe6\x9d\x83\xe9\x99\x90, \xe7\xb1\xbb\xe5\x9e\x8bID\xe8\xae\xbe\xe7\xbd\xae\xe4\xb8\x80\xe6\xa0\xb7', verbose_name=b'\xe7\xb1\xbb\xe5\x9e\x8bID')),
            ],
            options={
                'verbose_name': '\u6743\u9650',
                'verbose_name_plural': '\u6743\u9650',
            },
        ),
        migrations.CreateModel(
            name='ServerPassword',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('port', models.IntegerField(verbose_name=b'\xe7\xab\xaf\xe5\x8f\xa3')),
                ('username', models.CharField(blank=True, max_length=64, null=True, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe5\x90\x8d')),
                ('password', models.CharField(blank=True, max_length=64, null=True, verbose_name=b'\xe5\xaf\x86\xe7\xa0\x81')),
                ('ssh_key', models.CharField(blank=True, max_length=64, null=True, verbose_name=b'\xe7\xa7\x98\xe9\x92\xa5')),
            ],
            options={
                'verbose_name': '\u4e3b\u673a\u79d8\u94a5',
                'verbose_name_plural': '\u4e3b\u673a\u79d8\u94a5',
            },
        ),
        migrations.CreateModel(
            name='Servers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostname', models.CharField(max_length=255, unique=True, verbose_name=b'\xe4\xb8\xbb\xe6\x9c\xba\xe5\x90\x8d')),
                ('ip', models.GenericIPAddressField(unique=True, verbose_name=b'ip\xe5\x9c\xb0\xe5\x9d\x80')),
                ('mac', models.CharField(max_length=255, verbose_name=b'\xe7\x89\xa9\xe7\x90\x86\xe5\x9c\xb0\xe5\x9d\x80')),
                ('cpu', models.CharField(max_length=255, verbose_name=b'cpu')),
                ('mainboard', models.CharField(max_length=255, verbose_name=b'\xe4\xb8\xbb\xe6\x9d\xbf')),
                ('mem', models.CharField(max_length=255, verbose_name=b'\xe5\x86\x85\xe5\xad\x98')),
                ('disk', models.CharField(max_length=255, verbose_name=b'\xe7\xa3\x81\xe7\x9b\x98')),
                ('system', models.CharField(max_length=255, verbose_name=b'\xe7\xb3\xbb\xe7\xbb\x9f\xe4\xbf\xa1\xe6\x81\xaf')),
                ('is_connect', models.IntegerField(choices=[(1, '\u5df2\u8fde\u63a5'), (0, '\u672a\u8fde\u63a5')], default=0, verbose_name=b'\xe8\xae\xa4\xe8\xaf\x81\xe7\x8a\xb6\xe6\x80\x81')),
                ('exist_salt_minion', models.IntegerField(choices=[(1, '\u5df2\u5b89\u88c5'), (0, '\u672a\u5b89\u88c5')], default=0, verbose_name=b'salt-minion')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name=b'\xe4\xbf\xae\xe6\x94\xb9\xe6\x97\xb6\xe9\x97\xb4')),
                ('is_active', models.BooleanField(choices=[(1, '\u542f\u7528'), (0, '\u672a\u542f\u7528')], default=1, help_text=b'\xe4\xb8\xbb\xe6\x9c\xba\xe6\x98\xaf\xe5\x90\xa6\xe5\x90\xaf\xe7\x94\xa8', verbose_name=b'\xe5\x90\xaf\xe7\x94\xa8\xe7\x8a\xb6\xe6\x80\x81')),
                ('departments', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='web.Departments', verbose_name=b'\xe9\x83\xa8\xe9\x97\xa8')),
            ],
            options={
                'verbose_name': '\u4e3b\u673a\u7ba1\u7406',
                'verbose_name_plural': '\u4e3b\u673a\u7ba1\u7406',
            },
        ),
        migrations.CreateModel(
            name='UserAudit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doing_date', models.DateTimeField(auto_now=True, verbose_name=b'\xe4\xba\x8b\xe4\xbb\xb6\xe6\x97\xb6\xe9\x97\xb4')),
                ('doing_name', models.CharField(max_length=64, verbose_name=b'\xe4\xba\x8b\xe4\xbb\xb6\xe5\x90\x8d\xe7\xa7\xb0')),
                ('doing_type', models.CharField(max_length=64, verbose_name=b'\xe4\xba\x8b\xe4\xbb\xb6\xe7\xb1\xbb\xe5\x9e\x8b')),
                ('doing', models.TextField(max_length=1000, verbose_name=b'\xe4\xba\x8b\xe4\xbb\xb6\xe8\xaf\xa6\xe6\x83\x85')),
            ],
            options={
                'verbose_name': '\u7528\u6237\u64cd\u4f5c',
                'verbose_name_plural': '\u7528\u6237\u64cd\u4f5c',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32, unique=True, verbose_name=b'\xe8\xb4\xa6\xe6\x88\xb7\xe5\x90\x8d')),
                ('password', models.CharField(help_text=b'\xe8\xaf\xb7\xe6\xb3\xa8\xe6\x84\x8f\xef\xbc\x8c\xe8\xbe\x93\xe5\x85\xa5\xe6\x98\x8e\xe6\x96\x87\xe5\xaf\x86\xe7\xa0\x81\xe8\x87\xaa\xe5\x8a\xa8\xe4\xbf\x9d\xe5\xad\x98\xe4\xb8\xba\xe5\x8a\xa0\xe5\xaf\x86\xe5\x90\x8e\xe7\x9a\x84\xe5\xaf\x86\xe7\xa0\x81\xe3\x80\x82\xe4\xb8\x8d\xe8\xa6\x81\xe8\xbd\xbb\xe6\x98\x93\xe7\x82\xb9\xe5\x87\xbb\xe4\xbf\x9d\xe5\xad\x98\xe4\xbc\x9a\xe6\x94\xb9\xe6\x8e\x89\xe5\xaf\x86\xe7\xa0\x81\xe7\x9a\x84\xe3\x80\x82', max_length=100, verbose_name=b'\xe5\xaf\x86\xe7\xa0\x81')),
                ('nickname', models.CharField(max_length=32, verbose_name=b'\xe6\x98\xb5\xe7\xa7\xb0')),
                ('email', models.EmailField(max_length=254, verbose_name=b'\xe9\x82\xae\xe7\xae\xb1')),
                ('phone', models.CharField(max_length=32, verbose_name=b'\xe7\x94\xb5\xe8\xaf\x9d')),
                ('headimg', models.ImageField(default=b'upload/headimg/0/default.jpg', help_text=b'\xe5\x8f\xaf\xe9\x80\x89\xe9\xa1\xb9\xef\xbc\x8c\xe4\xb8\x8d\xe5\xa1\xab\xe4\xbd\xbf\xe7\x94\xa8\xe9\xbb\x98\xe8\xae\xa4\xe5\x9b\xbe\xe7\x89\x87\xe3\x80\x82', upload_to=b'upload/headimg/0', verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe5\xa4\xb4\xe5\x83\x8f')),
                ('departments', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='web.Departments', verbose_name=b'\xe9\x83\xa8\xe9\x97\xa8')),
                ('group', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='web.GroupProfile', verbose_name=b'\xe7\xbb\x84\xe5\x90\x8d')),
                ('permission', models.ManyToManyField(blank=True, to='web.Permission', verbose_name=b'\xe5\x8f\xaf\xe7\x94\xa8\xe6\x9d\x83\xe9\x99\x90')),
            ],
            options={
                'verbose_name': '\u7528\u6237',
                'verbose_name_plural': '\u7528\u6237',
            },
        ),
        migrations.AddField(
            model_name='useraudit',
            name='username',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='web.UserProfile', verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe5\x90\x8d'),
        ),
        migrations.AddField(
            model_name='serverpassword',
            name='hostname',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='web.Servers', verbose_name=b'\xe4\xb8\xbb\xe6\x9c\xba\xe5\x90\x8d'),
        ),
        migrations.AddField(
            model_name='groupprofile',
            name='permission',
            field=models.ManyToManyField(to='web.Permission', verbose_name=b'\xe5\x8f\xaf\xe7\x94\xa8\xe6\x9d\x83\xe9\x99\x90'),
        ),
    ]