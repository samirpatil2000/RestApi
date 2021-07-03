from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Text
from .forms import TextForm
def list_view(request):
    context={}
    if request.method=="GET":
        context['objects']=Text.objects.all()

    return render(request,'index.html',context)
def textDetail(request,slug):
    context={
        'objects':None,
        'object':Text.objects.get(slug=slug)
    }

    return render(request,'index.html',context)
import random
def createView(request):
    context={}
    forms=TextForm()
    if request.method=="POST":
        forms=TextForm(request.POST)
        if forms.is_valid():
            text=forms.save(commit=False)
            # text.slug=str(text.name)+str(random.randint(99,999))
            text.save()
            # print(text.slug,"888887878888888888888888888")
            return HttpResponse(text.slug)
    context['forms']=forms
    return render(request,'index.html',context)

