# encoding: utf-8
from __future__ import unicode_literals

from django.db import models


class TDaozhen(models.Model):
    daozhenid = models.AutoField(db_column='daozhenId', primary_key=True)  # Field name made lowercase.
    keshiid = models.IntegerField(db_column='keshiId', blank=True, null=True)  # Field name made lowercase.
    zhengzhuang = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 't_daozhen'


class TGuahao(models.Model):
    guahaoid = models.AutoField(db_column='guahaoId', primary_key=True)  # Field name made lowercase.
    bingrenid = models.IntegerField(db_column='bingrenId', blank=True, null=True)  # Field name made lowercase.
    addtime = models.DateField(db_column='addTime', blank=True, null=True)  # Field name made lowercase.
    yishengid = models.IntegerField(db_column='yishengId', blank=True, null=True)  # Field name made lowercase.
    zhengduan = models.CharField(max_length=255, blank=True, null=True)
    yaopin = models.CharField(max_length=255, blank=True, null=True)
    zhengduantime = models.DateField(db_column='zhengduanTime', blank=True, null=True)  # Field name made lowercase.
    keshiid = models.IntegerField(db_column='keshiId', blank=True, null=True)  # Field name made lowercase.
    guahaostatus = models.CharField(db_column='guahaoStatus', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 't_guahao'


class TKeshi(models.Model):
    keshiid = models.AutoField(db_column='keshiId', primary_key=True)  # Field name made lowercase.
    keshiname = models.CharField(db_column='keshiName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    bianhao = models.CharField(max_length=255, blank=True, null=True)
    didian = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 't_keshi'


class TUser(models.Model):
    userid = models.AutoField(db_column='userId', primary_key=True)  # Field name made lowercase.
    username = models.CharField(db_column='userName', max_length=20)  # Field name made lowercase.
    password = models.CharField(max_length=32)
    mobile = models.CharField(max_length=11, blank=True, null=True)
    updatetime = models.DateField(db_column='updateTime', blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(max_length=56, blank=True, null=True)
    realname = models.CharField(db_column='realName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sex = models.CharField(max_length=20, blank=True, null=True)
    age = models.CharField(max_length=20, blank=True, null=True)
    idcard = models.CharField(db_column='idCard', max_length=20, blank=True, null=True)  # Field name made lowercase.
    kahao = models.CharField(max_length=255, blank=True, null=True)
    yue = models.IntegerField(blank=True, null=True)
    gonghao = models.CharField(max_length=255, blank=True, null=True)
    keshiid = models.IntegerField(db_column='keshiId', blank=True, null=True)  # Field name made lowercase.
    suoshu = models.CharField(db_column='suoshu', max_length=20)

    class Meta:
        managed = True
        db_table = 't_user'


class TYaopin(models.Model):
    yaopinid = models.AutoField(db_column='yaopinId', primary_key=True)  # Field name made lowercase.
    yaopinname = models.CharField(db_column='yaopinName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    jiage = models.CharField(max_length=255, blank=True, null=True)
    shuliang = models.IntegerField(blank=True, null=True)
    bianhao = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 't_yaopin'


class Admin(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    pwd = models.CharField(max_length=50)


