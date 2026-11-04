from django.shortcuts import render,redirect
from actors.models import Actors
from actors.forms import ActorForm
from django.http import HttpResponse

# Create your views here.
def addActor(request):
    if request.method=="POST":
        form=ActorForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/")
        else:
            return HttpResponse("Invalid form data")
    else:
        form=ActorForm()
    
    return render(request,"add-actor.html",{"my_form":form})