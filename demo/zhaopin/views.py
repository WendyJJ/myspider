from django.shortcuts import render
from django.http import HttpResponse
from zhaopin.models import *
from django.core.paginator import Paginator

# Create your views here.
def index(request,pIndex):
    # return HttpResponse('Hello,Django!')
    # list = ZhaoPin.objects.raw('select * from liepin order by time_pub desc limit 1000')
    list = ZhaoPin.objects.filter(id__range=(1,1000))
    # print(type(list))
    # position = request.GET['position']
    p = Paginator(list,100)
    if pIndex == '':
        pIndex = '1'
    pIndex = int(pIndex)
    list2 = p.page(pIndex)
    plist = p.page_range
    maxnum = p.num_pages
    context = {
        'list':list2,'plist':plist,'pIndex':pIndex,'maxnum':maxnum,

    }
    return render(request,'index.html',context)

def search(request,pIndex):
    # return HttpResponse('ok')
    position = request.GET['position']
    edu = request.GET['edu']
    # print(position,edu)
    list = ZhaoPin.objects.filter()
    list = list.filter(pname__contains=position)
    list = list.filter(degree__contains=edu)
    p = Paginator(list,10)
    if pIndex == '':
        pIndex = '1'
    pIndex = int(pIndex)
    list2 = p.page(pIndex)
    plist = p.page_range
    maxnum = p.num_pages
    content = {
        'list':list2,'plist':plist,'pIndex':pIndex,'maxnum':maxnum,'position':position,'edu':edu
    }
    return  render(request,'search.html',content)