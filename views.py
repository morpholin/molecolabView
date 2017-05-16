from django.shortcuts import render,get_object_or_404
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse,JsonResponse
from django.template import loader
from django.templatetags.static import static

import json

from .models import Question

# Create your views here.

city =""
name=""
@csrf_protect
def ajax_input(request):
    global city
    global name
    if request.method == 'GET' and request.is_ajax():
        #name = request.POST.get('name')
        print "GET"
        dic = { "INFO" : { 0 : "hamster", 1 : "hello" , 2 : "du" }, "atoms" :{ 0: [ 'C',[1,2,3]], 1: ['H',[2,3,4]] } }
        return JsonResponse(dic)
    if request.method == 'POST' and request.is_ajax():
        print "POST"
        print request.POST['city']
        city = request.POST['city']
        name = request.POST['name']
        return HttpResponse("Hallo")
    else:
        return HttpResponse("HALLO %s aus %s" % (name,city))

@csrf_protect
def blog(request):
    template = loader.get_template('blog.html')
    context = {
     'Figure' : "hey"
    }
    return HttpResponse(template.render(context,request))

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'detail.html',{'question': question})
