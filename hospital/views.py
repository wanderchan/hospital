# encoding: utf-8
from django.shortcuts import render
import datetime
import re
from hospital import commons
from hospital import models
from django.http import HttpResponseRedirect
from django.db.models import Sum
# Create your views here.
def admin(request):
    money = models.TUser.objects.aggregate(Sum('yue'))
    money = str(money)
    money = re.search(':(.*?)}', money, re.M).group(1)
    renshu = models.TUser.objects.filter(type='患者').count()
    zongrenshu = models.TUser.objects.all().count()
    d1 = datetime.date.today()
    jinguahao = models.TGuahao.objects.filter(addtime=d1).count()
    d2 = str(d1 - datetime.timedelta(days=1))
    d3 = str(d1 - datetime.timedelta(days=2))
    d4 = str(d1 - datetime.timedelta(days=3))
    d5 = str(d1 - datetime.timedelta(days=4))
    d6 = str(d1 - datetime.timedelta(days=5))
    d7 = str(d1 - datetime.timedelta(days=6))
    d0 = str(d1)
    d2g = str(models.TGuahao.objects.filter(addtime=d2).count())
    d3g = str(models.TGuahao.objects.filter(addtime=d3).count())
    d4g = str(models.TGuahao.objects.filter(addtime=d4).count())
    d5g = str(models.TGuahao.objects.filter(addtime=d5).count())
    d6g = str(models.TGuahao.objects.filter(addtime=d6).count())
    d7g = str(models.TGuahao.objects.filter(addtime=d7).count())
    k1 = models.TKeshi.objects.get(keshiid=1).keshiname
    k2 = models.TKeshi.objects.get(keshiid=2).keshiname
    k3 = models.TKeshi.objects.get(keshiid=3).keshiname
    k4 = models.TKeshi.objects.get(keshiid=4).keshiname
    k5 = models.TKeshi.objects.get(keshiid=5).keshiname
    neike = models.TGuahao.objects.filter(keshiid='1').count()
    waike = models.TGuahao.objects.filter(keshiid='2').count()
    erbihou = models.TGuahao.objects.filter(keshiid='3').count()
    yake = models.TGuahao.objects.filter(keshiid='4').count()
    yanke = models.TGuahao.objects.filter(keshiid='5').count()
    neike1 = models.TUser.objects.filter(keshiid='1').count()
    waike1 = models.TUser.objects.filter(keshiid='2').count()
    erbihou1 = models.TUser.objects.filter(keshiid='3').count()
    yake1 = models.TUser.objects.filter(keshiid='4').count()
    yanke1 = models.TUser.objects.filter(keshiid='5').count()
    ke1wd1 = models.TGuahao.objects.filter(keshiid='1',addtime=d1,guahaostatus='未处理').count()
    ke1yd1 = models.TGuahao.objects.filter(keshiid='1',addtime=d1,guahaostatus='已处理').count()
    ke1wd2 = models.TGuahao.objects.filter(keshiid='1',addtime=d2,guahaostatus='未处理').count()
    ke1yd2 = models.TGuahao.objects.filter(keshiid='1',addtime=d2,guahaostatus='已处理').count()
    ke1wd3 = models.TGuahao.objects.filter(keshiid='1',addtime=d3,guahaostatus='未处理').count()
    ke1yd3 = models.TGuahao.objects.filter(keshiid='1',addtime=d3,guahaostatus='已处理').count()
    ke1wd4 = models.TGuahao.objects.filter(keshiid='1',addtime=d4,guahaostatus='未处理').count()
    ke1yd4 = models.TGuahao.objects.filter(keshiid='1',addtime=d4,guahaostatus='已处理').count()
    ke1wd5 = models.TGuahao.objects.filter(keshiid='1',addtime=d5,guahaostatus='未处理').count()
    ke1yd5 = models.TGuahao.objects.filter(keshiid='1',addtime=d5,guahaostatus='已处理').count()
    ke1wd6 = models.TGuahao.objects.filter(keshiid='1',addtime=d6,guahaostatus='未处理').count()
    ke1yd6 = models.TGuahao.objects.filter(keshiid='1',addtime=d6,guahaostatus='已处理').count()
    ke1wd7 = models.TGuahao.objects.filter(keshiid='1',addtime=d7,guahaostatus='未处理').count()
    ke1yd7 = models.TGuahao.objects.filter(keshiid='1',addtime=d7,guahaostatus='已处理').count()
    ke2wd1 = models.TGuahao.objects.filter(keshiid='2',addtime=d1,guahaostatus='未处理').count()
    ke2yd1 = models.TGuahao.objects.filter(keshiid='2',addtime=d1,guahaostatus='已处理').count()
    ke2wd2 = models.TGuahao.objects.filter(keshiid='2',addtime=d2,guahaostatus='未处理').count()
    ke2yd2 = models.TGuahao.objects.filter(keshiid='2',addtime=d2,guahaostatus='已处理').count()
    ke2wd3 = models.TGuahao.objects.filter(keshiid='2',addtime=d3,guahaostatus='未处理').count()
    ke2yd3 = models.TGuahao.objects.filter(keshiid='2',addtime=d3,guahaostatus='已处理').count()
    ke2wd4 = models.TGuahao.objects.filter(keshiid='2',addtime=d4,guahaostatus='未处理').count()
    ke2yd4 = models.TGuahao.objects.filter(keshiid='2',addtime=d4,guahaostatus='已处理').count()
    ke2wd5 = models.TGuahao.objects.filter(keshiid='2',addtime=d5,guahaostatus='未处理').count()
    ke2yd5 = models.TGuahao.objects.filter(keshiid='2',addtime=d5,guahaostatus='已处理').count()
    ke2wd6 = models.TGuahao.objects.filter(keshiid='2',addtime=d6,guahaostatus='未处理').count()
    ke2yd6 = models.TGuahao.objects.filter(keshiid='2',addtime=d6,guahaostatus='已处理').count()
    ke2wd7 = models.TGuahao.objects.filter(keshiid='2',addtime=d7,guahaostatus='未处理').count()
    ke2yd7 = models.TGuahao.objects.filter(keshiid='2',addtime=d7,guahaostatus='已处理').count()
    ke3wd1 = models.TGuahao.objects.filter(keshiid='3',addtime=d1,guahaostatus='未处理').count()
    ke3yd1 = models.TGuahao.objects.filter(keshiid='3',addtime=d1,guahaostatus='已处理').count()
    ke3wd2 = models.TGuahao.objects.filter(keshiid='3',addtime=d2,guahaostatus='未处理').count()
    ke3yd2 = models.TGuahao.objects.filter(keshiid='3',addtime=d2,guahaostatus='已处理').count()
    ke3wd3 = models.TGuahao.objects.filter(keshiid='3',addtime=d3,guahaostatus='未处理').count()
    ke3yd3 = models.TGuahao.objects.filter(keshiid='3',addtime=d3,guahaostatus='已处理').count()
    ke3wd4 = models.TGuahao.objects.filter(keshiid='3',addtime=d4,guahaostatus='未处理').count()
    ke3yd4 = models.TGuahao.objects.filter(keshiid='3',addtime=d4,guahaostatus='已处理').count()
    ke3wd5 = models.TGuahao.objects.filter(keshiid='3',addtime=d5,guahaostatus='未处理').count()
    ke3yd5 = models.TGuahao.objects.filter(keshiid='3',addtime=d5,guahaostatus='已处理').count()
    ke3wd6 = models.TGuahao.objects.filter(keshiid='3',addtime=d6,guahaostatus='未处理').count()
    ke3yd6 = models.TGuahao.objects.filter(keshiid='3',addtime=d6,guahaostatus='已处理').count()
    ke3wd7 = models.TGuahao.objects.filter(keshiid='3',addtime=d7,guahaostatus='未处理').count()
    ke3yd7 = models.TGuahao.objects.filter(keshiid='3',addtime=d7,guahaostatus='已处理').count()
    ke4wd1 = models.TGuahao.objects.filter(keshiid='4',addtime=d1,guahaostatus='未处理').count()
    ke4yd1 = models.TGuahao.objects.filter(keshiid='4',addtime=d1,guahaostatus='已处理').count()
    ke4wd2 = models.TGuahao.objects.filter(keshiid='4',addtime=d2,guahaostatus='未处理').count()
    ke4yd2 = models.TGuahao.objects.filter(keshiid='4',addtime=d2,guahaostatus='已处理').count()
    ke4wd3 = models.TGuahao.objects.filter(keshiid='4',addtime=d3,guahaostatus='未处理').count()
    ke4yd3 = models.TGuahao.objects.filter(keshiid='4',addtime=d3,guahaostatus='已处理').count()
    ke4wd4 = models.TGuahao.objects.filter(keshiid='4',addtime=d4,guahaostatus='未处理').count()
    ke4yd4 = models.TGuahao.objects.filter(keshiid='4',addtime=d4,guahaostatus='已处理').count()
    ke4wd5 = models.TGuahao.objects.filter(keshiid='4',addtime=d5,guahaostatus='未处理').count()
    ke4yd5 = models.TGuahao.objects.filter(keshiid='4',addtime=d5,guahaostatus='已处理').count()
    ke4wd6 = models.TGuahao.objects.filter(keshiid='4',addtime=d6,guahaostatus='未处理').count()
    ke4yd6 = models.TGuahao.objects.filter(keshiid='4',addtime=d6,guahaostatus='已处理').count()
    ke4wd7 = models.TGuahao.objects.filter(keshiid='4',addtime=d7,guahaostatus='未处理').count()
    ke4yd7 = models.TGuahao.objects.filter(keshiid='4',addtime=d7,guahaostatus='已处理').count()
    ke5wd1 = models.TGuahao.objects.filter(keshiid='5',addtime=d1,guahaostatus='未处理').count()
    ke5yd1 = models.TGuahao.objects.filter(keshiid='5',addtime=d1,guahaostatus='已处理').count()
    ke5wd2 = models.TGuahao.objects.filter(keshiid='5',addtime=d2,guahaostatus='未处理').count()
    ke5yd2 = models.TGuahao.objects.filter(keshiid='5',addtime=d2,guahaostatus='已处理').count()
    ke5wd3 = models.TGuahao.objects.filter(keshiid='5',addtime=d3,guahaostatus='未处理').count()
    ke5yd3 = models.TGuahao.objects.filter(keshiid='5',addtime=d3,guahaostatus='已处理').count()
    ke5wd4 = models.TGuahao.objects.filter(keshiid='5',addtime=d4,guahaostatus='未处理').count()
    ke5yd4 = models.TGuahao.objects.filter(keshiid='5',addtime=d4,guahaostatus='已处理').count()
    ke5wd5 = models.TGuahao.objects.filter(keshiid='5',addtime=d5,guahaostatus='未处理').count()
    ke5yd5 = models.TGuahao.objects.filter(keshiid='5',addtime=d5,guahaostatus='已处理').count()
    ke5wd6 = models.TGuahao.objects.filter(keshiid='5',addtime=d6,guahaostatus='未处理').count()
    ke5yd6 = models.TGuahao.objects.filter(keshiid='5',addtime=d6,guahaostatus='已处理').count()
    ke5wd7 = models.TGuahao.objects.filter(keshiid='5',addtime=d7,guahaostatus='未处理').count()
    ke5yd7 = models.TGuahao.objects.filter(keshiid='5',addtime=d7,guahaostatus='已处理').count()

    return render(request, "admin.html",{"money":money,'huanzherenshu':renshu,'zongrenshu':zongrenshu,'jinguahao':jinguahao\
                                         ,"d1":d0,'d2':d2,"d3":d3,'d4':d4,"d5":d5,'d6':d6,'d7':d7,'d2g':d2g,"d3g":d3g,'d4g':d4g,\
                                         "d5g":d5g,'d6g':d6g,'d7g':d7g,'neike':neike,'waike':waike,'erbihou':erbihou,'yake':yake,\
                                         'yanke':yanke,'neike1':neike1,'waike1':waike1,'erbihou1':erbihou1,'yake1':yake1,\
                                         'yanke1':yanke1,'k1':k1,'k2':k2,'k3':k3,'k4':k4,'k5':k5,'ke1wd1':ke1wd1,'ke1yd1':ke1yd1, \
                                         'ke1wd2': ke1wd2, 'ke1yd2': ke1yd2,'ke1wd3':ke1wd3,'ke1yd3':ke1yd3,'ke1wd4':ke1wd4,'ke1yd4':ke1yd4, \
                                         'ke1wd5': ke1wd5, 'ke1yd5': ke1yd5,'ke1wd6':ke1wd6,'ke1yd6':ke1yd6,'ke1wd7':ke1wd7,'ke1yd7':ke1yd7, \
                                         'ke2wd1': ke2wd1, 'ke2yd1': ke2yd1, 'ke2wd2': ke2wd2, 'ke2yd2': ke2yd2, 'ke2wd3': ke2wd3, 'ke2yd3': ke2yd3,\
                                         'ke2wd4': ke2wd4, 'ke2yd4': ke2yd4,'ke2wd5': ke2wd5, 'ke2yd5': ke2yd5, 'ke2wd6': ke2wd6, 'ke2yd6': ke2yd6,\
                                         'ke2wd7': ke2wd7, 'ke2yd7': ke2yd7, \
                                         'ke3wd1': ke3wd1, 'ke3yd1': ke3yd1, 'ke3wd2': ke3wd2, 'ke3yd2': ke3yd2,'ke3wd3': ke3wd3, 'ke3yd3': ke3yd3, \
                                         'ke3wd4': ke3wd4, 'ke3yd4': ke3yd4, 'ke3wd5': ke3wd5, 'ke3yd5': ke3yd5,'ke3wd6': ke3wd6, 'ke3yd6': ke3yd6, \
                                         'ke3wd7': ke3wd7, 'ke3yd7': ke3yd7, \
                                         'ke4wd1': ke4wd1, 'ke4yd1': ke4yd1, 'ke4wd2': ke4wd2, 'ke4yd2': ke4yd2,'ke4wd3': ke4wd3, 'ke4yd3': ke4yd3, \
                                         'ke4wd4': ke4wd4, 'ke4yd4': ke4yd4, 'ke4wd5': ke4wd5, 'ke4yd5': ke4yd5,'ke4wd6': ke4wd6, 'ke4yd6': ke4yd6, \
                                         'ke4wd7': ke4wd7, 'ke4yd7': ke4yd7, \
                                         'ke5wd1': ke5wd1, 'ke5yd1': ke5yd1, 'ke5wd2': ke5wd2, 'ke5yd2': ke5yd2,'ke5wd3': ke5wd3, 'ke5yd3': ke5yd3, \
                                         'ke5wd4': ke5wd4, 'ke5yd4': ke5yd4, 'ke5wd5': ke5wd5, 'ke5yd5': ke5yd5,'ke5wd6': ke5wd6, 'ke5yd6': ke5yd6, \
                                         'ke5wd7': ke5wd7, 'ke5yd7': ke5yd7, \
                                         })

def guahao(request):
    if request.method == "POST":
        if request.POST.get("id",None) == None:
            if request.POST.get("quxiao",None) == None:
                ghuserid =request.POST.get("ghuserid")
                addtime = request.POST.get("addtime",None)
                yishengid = request.POST.get("yishengid",None)
                zhengduan = request.POST.get("zhengduan",None)
                yaopin = request.POST.get("yaopin",None)
                zhengduantime = request.POST.get("zhengduantime",None)
                keshiid = request.POST.get("keshiid",None)
                guahaostatus = request.POST.get("guahaostatus",None)
                models.TGuahao.objects.create(bingrenid=ghuserid, addtime=addtime, yishengid=yishengid ,zhengduan=zhengduan, \
                                            yaopin=yaopin, zhengduantime=zhengduantime, keshiid=keshiid, guahaostatus=guahaostatus)
                gh = models.TGuahao.objects.filter(bingrenid=ghuserid)
                name = models.TUser.objects.get(userid=ghuserid)
            if request.POST.get("quxiao") == '3':
                ghuserid = request.POST.get("ghuserid")
                shanchuid = request.POST.get("shanchuid")
                models.TGuahao.objects.filter(guahaoid=shanchuid).delete()
                gh = models.TGuahao.objects.filter(bingrenid=ghuserid)
                name = models.TUser.objects.get(userid=ghuserid)
            if request.POST.get("quxiao") == '2':
                ghuserid =request.POST.get("ghuserid")
                xiugaiid = request.POST.get("xiugaiid")
                addtime = request.POST.get("addtime",None)
                yishengid = request.POST.get("yishengid",None)
                zhengduan = request.POST.get("zhengduan",None)
                yaopin = request.POST.get("yaopin",None)
                zhengduantime = request.POST.get("zhengduantime",None)
                keshiid = request.POST.get("keshiid",None)
                guahaostatus = request.POST.get("guahaostatus",None)
                models.TGuahao.objects.filter(guahaoid=xiugaiid).update(addtime=addtime, yishengid=yishengid ,zhengduan=zhengduan, \
                                            yaopin=yaopin, zhengduantime=zhengduantime, keshiid=keshiid, guahaostatus=guahaostatus)
                gh = models.TGuahao.objects.filter(bingrenid=ghuserid)
                name = models.TUser.objects.get(userid=ghuserid)
        else:
            id = request.POST.get("id")
            gh = models.TGuahao.objects.filter(bingrenid=id)
            name = models.TUser.objects.get(userid=id)
    return render(request,"guahao.html",{'data':gh ,'name':name})

def bingren(request):
    if request.method =="POST":
        if request.POST.get("id", None) == None:
            username = request.POST.get("username",None)
            password = request.POST.get("password",None)
            mobile = request.POST.get("mobile",None)
            updatetime = request.POST.get("updatetime",None)
            realname = request.POST.get("realname",None)
            sex = request.POST.get("sex",None)
            age = request.POST.get("age",None)
            idcard = request.POST.get("idcard",None)
            yue = request.POST.get("yue",None)
            suoshu = request.POST.get("suoshu", None)
            models.TUser.objects.create(username=username, password=password, mobile=mobile ,updatetime=updatetime, \
                                        realname=realname, sex=sex, age=age, idcard=idcard, \
                                        yue=yue, suoshu=suoshu, type='患者')
        else:
            if request.POST.get("quxiao") == '3':
                id = request.POST.get("id", None)
                username = request.POST.get("username", None)
                password = request.POST.get("password", None)
                mobile = request.POST.get("mobile", None)
                updatetime = request.POST.get("updatetime", None)
                realname = request.POST.get("realname", None)
                sex = request.POST.get("sex", None)
                age = request.POST.get("age", None)
                idcard = request.POST.get("idcard", None)
                yue = request.POST.get("yue", None)
                suoshu = request.POST.get("suoshu", None)
                models.TUser.objects.filter(userid=id).update(username=username, password=password, mobile=mobile, updatetime=updatetime, \
                                            realname=realname, sex=sex, age=age, idcard=idcard, \
                                            yue=yue, suoshu=suoshu)
            if request.POST.get("quxiao", None) == None:
                id = request.POST.get("id",None)
                models.TUser.objects.filter(userid=id).delete()
    pingren_list = models.TUser.objects.filter(type='患者')
    return render(request, "bingren.html",{"data":pingren_list})

def yiyuan(request):
    if request.method =="POST":
        if request.POST.get("id", None) == None:
            username = request.POST.get("username",None)
            password = request.POST.get("password",None)
            mobile = request.POST.get("mobile",None)
            updatetime = request.POST.get("updatetime",None)
            realname = request.POST.get("realname",None)
            sex = request.POST.get("sex",None)
            age = request.POST.get("age",None)
            gonghao = request.POST.get("gonghao",None)
            suoshu = request.POST.get("suoshu", None)
            models.TUser.objects.create(username=username, password=password, mobile=mobile ,updatetime=updatetime, \
                                        realname=realname, sex=sex, age=age, gonghao=gonghao, \
                                        suoshu=suoshu, type='医生')
        else:
            if request.POST.get("quxiao")== '1':
                id = request.POST.get("id", None)
                models.TUser.objects.filter(userid=id).update(type="医生")
            if request.POST.get("quxiao")=='2':
                id = request.POST.get("id", None)
                models.TUser.objects.filter(userid=id).update(type="管理员")
            if request.POST.get("quxiao") == '3':
                id = request.POST.get("id", None)
                username = request.POST.get("username", None)
                password = request.POST.get("password", None)
                mobile = request.POST.get("mobile", None)
                updatetime = request.POST.get("updatetime", None)
                realname = request.POST.get("realname", None)
                sex = request.POST.get("sex", None)
                age = request.POST.get("age", None)
                gonghao = request.POST.get("gonghao", None)
                suoshu = request.POST.get("suoshu", None)
                models.TUser.objects.filter(userid=id).update(username=username, password=password, mobile=mobile, updatetime=updatetime, \
                                            realname=realname, sex=sex, age=age, gonghao=gonghao, suoshu=suoshu)
            if request.POST.get("quxiao", None) == None:
                id = request.POST.get("id",None)
                models.TUser.objects.filter(userid=id).delete()
    yisheng_list = models.TUser.objects.filter(type = '医生')
    yiguanli_list = models.TUser.objects.filter(type='管理员')
    return render(request, "yiyuan.html",{"data":yisheng_list,'gldata':yiguanli_list})

def guanli(request):
    return render(request, "guanli.html",)

def keshi(request):
    if request.method =="POST":
        if request.POST.get("id", None) == None:
            keshiname = request.POST.get("keshiname",None)
            bianhao = request.POST.get("bianhao",None)
            didian = request.POST.get("didian",None)
            models.TKeshi.objects.create(keshiname=keshiname, bianhao=bianhao, didian=didian)
        else:
            if request.POST.get("quxiao") == '3':
                id = request.POST.get("id", None)
                keshiname = request.POST.get("keshiname", None)
                bianhao = request.POST.get("bianhao", None)
                didian = request.POST.get("didian", None)
                models.TKeshi.objects.filter(keshiid=id).update(keshiname=keshiname, bianhao=bianhao, didian=didian)
            if request.POST.get("quxiao", None) == None:
                id = request.POST.get("id",None)
                models.TKeshi.objects.filter(keshiid=id).delete()
    keshi_list = models.TKeshi.objects.all()
    return render(request, "keshi.html", {'data': keshi_list})

def yaopin(request):
    if request.method =="POST":
        if request.POST.get("id",None)== None:
            yaopinname = request.POST.get("yaopinname",None)
            jiage = request.POST.get("jiage",None)
            shuliang = request.POST.get("shuliang",None)
            bianhao = request.POST.get("bianhao", None)
            models.TYaopin.objects.create(yaopinname=yaopinname, jiage=jiage, shuliang=shuliang, bianhao=bianhao)
        else:
            if request.POST.get("quxiao") == '3':
                id = request.POST.get("id", None)
                yaopinname = request.POST.get("yaopinname", None)
                jiage = request.POST.get("jiage", None)
                shuliang = request.POST.get("shuliang", None)
                bianhao = request.POST.get("bianhao", None)
                models.TYaopin.objects.filter(yaopinid=id).update(yaopinname=yaopinname, jiage=jiage, shuliang=shuliang, bianhao=bianhao)
            if request.POST.get("quxiao", None) == None:
                id = request.POST.get("id",None)
                models.TYaopin.objects.filter(yaopinid=id).delete()
    yaopin_list = models.TYaopin.objects.all()
    return render(request, "yaopin.html", {'data': yaopin_list})

def index(request):
    return render(request, "index.html")


def get_code(request):
    ca = commons.Captcha(request)
    ca.type = 'number'
    ca.img_width = 150
    ca.img_height = 30
    return ca.display()


def ajax_login(request):
    imgcode = request.GET.get("code")
    if not imgcode or imgcode == "":
        return commons.res_fail(1, "验证码不能为空")

    ca = commons.Captcha(request)
    if ca.check(imgcode):

        name = request.GET.get("name")
        pwd = request.GET.get("pwd")
        user_list = models.Admin.objects.get(id=1)
        name1 =user_list.name
        pwd1 = user_list.pwd
        if name ==name1 and pwd ==pwd1 :
            return commons.res_success("登录成功")
        else:
            return commons.res_fail(1, "用户或密码不正确")

    else:
        return commons.res_fail(1, "验证码不正确")



def ajax_admin_updatepwd(request):
    # 需要登录才可以访问

    guanli_list = models.Admin.objects.get(id='1')
    curr_admin = guanli_list.name
    old_pwd = request.GET.get("old_pwd")
    pwd = request.GET.get("pwd")
    pwd2 = request.GET.get("pwd2")

    if old_pwd == "":
        return commons.res_fail(1, "旧密码不能为空")
    if pwd == "":
        return commons.res_fail(1, "新密码不能为空")
    if pwd != pwd2:
        return commons.res_fail(1, "确认密码不正确")

    try:
        admin = models.Admin.objects.get(name=curr_admin, pwd=old_pwd)
        admin.pwd = pwd
        admin.save()

        return commons.res_success("修改密码成功")
    except:
        return commons.res_fail(1, "旧密码不正确")