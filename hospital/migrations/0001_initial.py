# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-05-21 05:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('pwd', models.CharField(max_length=50)),
                ('add_time', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='TDaozhen',
            fields=[
                ('daozhenid', models.AutoField(db_column='daozhenId', primary_key=True, serialize=False)),
                ('keshiid', models.IntegerField(blank=True, db_column='keshiId', null=True)),
                ('zhengzhuang', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 't_daozhen',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TGuahao',
            fields=[
                ('guahaoid', models.AutoField(db_column='guahaoId', primary_key=True, serialize=False)),
                ('bingrenid', models.IntegerField(blank=True, db_column='bingrenId', null=True)),
                ('addtime', models.DateField(blank=True, db_column='addTime', null=True)),
                ('yishengid', models.IntegerField(blank=True, db_column='yishengId', null=True)),
                ('zhengduan', models.CharField(blank=True, max_length=255, null=True)),
                ('yaopin', models.CharField(blank=True, max_length=255, null=True)),
                ('zhengduantime', models.DateField(blank=True, db_column='zhengduanTime', null=True)),
                ('keshiid', models.IntegerField(blank=True, db_column='keshiId', null=True)),
                ('guahaostatus', models.CharField(blank=True, db_column='guahaoStatus', max_length=255, null=True)),
            ],
            options={
                'db_table': 't_guahao',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TKeshi',
            fields=[
                ('keshiid', models.AutoField(db_column='keshiId', primary_key=True, serialize=False)),
                ('keshiname', models.CharField(blank=True, db_column='keshiName', max_length=255, null=True)),
                ('bianhao', models.CharField(blank=True, max_length=255, null=True)),
                ('didian', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 't_keshi',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TUser',
            fields=[
                ('userid', models.AutoField(db_column='userId', primary_key=True, serialize=False)),
                ('username', models.CharField(db_column='userName', max_length=20)),
                ('password', models.CharField(max_length=32)),
                ('mobile', models.CharField(blank=True, max_length=11, null=True)),
                ('updatetime', models.DateField(blank=True, db_column='updateTime', null=True)),
                ('type', models.CharField(blank=True, max_length=56, null=True)),
                ('realname', models.CharField(blank=True, db_column='realName', max_length=255, null=True)),
                ('sex', models.CharField(blank=True, max_length=20, null=True)),
                ('age', models.CharField(blank=True, max_length=20, null=True)),
                ('idcard', models.CharField(blank=True, db_column='idCard', max_length=20, null=True)),
                ('kahao', models.CharField(blank=True, max_length=255, null=True)),
                ('yue', models.IntegerField(blank=True, null=True)),
                ('gonghao', models.CharField(blank=True, max_length=255, null=True)),
                ('keshiid', models.IntegerField(blank=True, db_column='keshiId', null=True)),
            ],
            options={
                'db_table': 't_user',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TYaopin',
            fields=[
                ('yaopinid', models.AutoField(db_column='yaopinId', primary_key=True, serialize=False)),
                ('yaopinname', models.CharField(blank=True, db_column='yaopinName', max_length=255, null=True)),
                ('jiage', models.CharField(blank=True, max_length=255, null=True)),
                ('shuliang', models.IntegerField(blank=True, null=True)),
                ('bianhao', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 't_yaopin',
                'managed': True,
            },
        ),
    ]
