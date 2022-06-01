from django.shortcuts import render



# from django.http import HttpResponse
# from django.template import loader

from .models import Bb

def index(request):
    # # return HttpResponse("Здесь будет текст...")
    # template=loader.get_template('firstApp/termplates/index.html')
    bbs=Bb.objects.order_by('-published')
    context= {'bbs': bbs}
    # return HttpResponse(template.render(context,request))
# from django.shortcuts import render

# def index(request):
#     return render(request, 'firstApp/index.html')
    return render(request,'index.html',context)
