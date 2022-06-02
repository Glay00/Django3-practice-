from django.shortcuts import render

from  django.views.generic.edit import CreateView
# from django.http import HttpResponse
# from django.template import loader
from .forms import BbForm
from .models import Bb, Rubric

def index(request):
    # # return HttpResponse("Здесь будет текст...")
    # template=loader.get_template('firstApp/termplates/index.html')
    bbs=Bb.objects.all()
    context= {'bbs': bbs}
    # return HttpResponse(template.render(context,request))
# from django.shortcuts import render

# def index(request):
#     return render(request, 'firstApp/index.html')
    return render(request,'index.html',context)

def by_rubric(request,rubric_id):
    bbs=Bb.objects.filter(rubric=rubric_id)
    rubrics=Rubric.objects.all()
    current_rubric=Rubric.objects.get(pk=rubric_id)
    context={'bbs':bbs, 'rubrics':rubrics,
            'current_rubric':current_rubric}
    return render(request,'by_rubric.html',context) #firstApp/by_rubric.html
    
class BbCreateView(CreateView):
    template_name: 'firstApp/create.html'
    form_class=BbForm
    success_url='firstApp'
