from django.shortcuts import render,redirect
from actors.models import Actors
from actors.forms import ActorForm
from django.http import HttpResponse
from django.views.generic import ListView,CreateView,DetailView,UpdateView,DeleteView
from django.urls import reverse_lazy
# Create your views here.
# def addActor(request):
#     if request.method=="POST":
#         form=ActorForm(request.POST,request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect("/")
#         else:
#             return HttpResponse("Invalid form data")
#     else:
#         form=ActorForm()
    
#     return render(request,"add-actor.html",{"my_form":form})

class AddActor(CreateView):
    models=Actors
    template_name="add-actor.html"
    form_class=ActorForm
    success_url=reverse_lazy("list_actors")


class AllActors(ListView):
    model=Actors
    template_name="list-actors.html"
    context_object_name="actors"
    
    
class UpdateActor(UpdateView):
    model=Actors
    form_class=ActorForm
    template_name="update-actors.html"
    success_url=reverse_lazy("list_actors")  
    
class ActorDetail(DetailView):
    model=Actors
    context_object_name="actor"
    template_name="actor-detail.html"
    
    
class DeleteActor(DeleteView):
    model=Actors
    success_url=reverse_lazy("list_actors")  