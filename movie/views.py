from django.shortcuts import render,redirect
from movie.models import Category
from movie.models import Movie
from django.http import HttpResponse
# Create your views here.


def addMovie(request):
    if request.method=="POST":
        movie=request.POST["movie"]
        tr_link=request.POST['trailer_link']
        cate=request.POST['category']
        re_date=request.POST['release_date']
        poster=request.FILES["poster"]
        desc=request.POST["description"]
        rating=request.POST["rating"]
        category=Category.objects.get(id=cate)
        Movie(movie=movie,trailer_link=tr_link,
              category=category,release_date=re_date,
              poster=poster,description=desc,rating=rating).save()
        return redirect("movie_list")
    
    categories=Category.objects.all()
    return render(request,"add-movie.html",{"categories":categories})

def movieList(request):
    movies = Movie.objects.all()

    return render(request, "movie-list.html", {
        "movies": movies
    })

def movieDetails(request, id):
    movie = Movie.objects.get(id=id)

    return render(request, "movie-details.html", {
        "movie": movie
    })
    
def deleteMovie(request, id):
    if request.method == "POST":
        movie = Movie.objects.get(id=id)
        movie.delete()

    return redirect("movie_list")