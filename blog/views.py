import json

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from blog.models import Leaderboard


def hello(request):
    return HttpResponse('hello')

def fraction_upload(request, name, number):
    """
    客户端上传客户端号和分数
    :param request:
    :param name: 客户端名字
    :param number: 分数
    :return:
    """
    re_dict = {"res":'', 'msg': 200}
    if name and number:
        try:
            lead, created = Leaderboard.objects.update_or_create(name=str(name), defaults={'fraction': int(number)})
            re_dict['res'] = '客户端:' + lead.name + ',分数:' + str(lead.fraction)
        except Exception as e:
            print(e)
            re_dict['res'] = '出错啦'
            re_dict['msg'] = 500
    else:
        re_dict['msg'] = 500
        re_dict['res'] = '没有这个客户端'

    return HttpResponse(json.dumps(re_dict))

def fraction_inqurie(request, start, end, name):
    """
    客户端查询
    :param request:
    :param start: 开始名次
    :param end: 结束名次
    :return:
    """
    re_dict = {"res":'', 'msg': 200}
    if start and end and name:
        try:
            starts = int(start)
            ends = int(end)
            leads = Leaderboard.objects.all().order_by('-fraction')[starts-1:ends]
            lead_list = [{'name': board.name, 'fraction':board.fraction} for board in leads]
            l_data = Leaderboard.objects.get(name=name)
            lead_list.append({'name': l_data.name, 'fraction': l_data.fraction})
            re_dict['res'] = lead_list
        except Exception as e:
            print(e)
            re_dict['res'] = '出错啦'
            re_dict['msg'] = 500
    else:
        re_dict['msg'] = 500
        re_dict['res'] = '请输入正确的名次'
    return HttpResponse(json.dumps(re_dict))
