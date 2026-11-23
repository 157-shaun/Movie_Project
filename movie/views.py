from django.shortcuts import render,redirect,get_object_or_404
from movie.models import Category
from movie.models import Movie
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from actors.models import Actors
from movie.models import MovieCast
from accounts.decorators import superuser_required
# Create your views here.


def home(request):
    return render(request,"index.html")


@superuser_required
def addMovie(request):
    if request.method == "POST":

        # Get movie details
        movie_name = request.POST["movie"]
        tr_link = request.POST["trailer_link"]
        cate = request.POST["category"]
        re_date = request.POST["release_date"]
        poster = request.FILES["poster"]
        desc = request.POST["description"]
        rating = request.POST["rating"]

        # Get category
        category = Category.objects.get(id=cate)

        # Save movie
        new_movie = Movie.objects.create(
            movie=movie_name,
            trailer_link=tr_link,
            category=category,
            release_date=re_date,
            poster=poster,
            description=desc,
            rating=rating
        )

        # Get selected actors and character names
        actor_ids = request.POST.getlist("actor_ids")
        character_names = request.POST.getlist("character_names")

        # Save movie cast
        for actor_id, character_name in zip(actor_ids, character_names):
            if actor_id and character_name.strip():
                MovieCast.objects.create(
                    movie=new_movie,
                    actor_id=actor_id,
                    character_name=character_name.strip()
                )

        return redirect("movie_list")

    categories = Category.objects.all()
    actors = Actors.objects.all()

    return render(request, "add-movie.html", {
        "categories": categories,
        "actors": actors
    })


def movieList(request):
    movies = Movie.objects.all()

    return render(request, "movie-list.html", {
        "movies": movies
    })
@ login_required(login_url="login")
def movieDetails(request, id):
    movie = get_object_or_404(Movie, id=id)
    cast = MovieCast.objects.filter(movie=movie).select_related('actor')

    return render(request, "movie-details.html", {
        "movie": movie,
        "cast": cast
    })
@superuser_required
def deleteMovie(request, id):
    movie = Movie.objects.get(id=id)
    movie.delete()

    return redirect("movie_list")

def category_movies(request, slug):
    category = get_object_or_404(Category, slug=slug)
    movies = Movie.objects.filter(category=category)
    return render(
        request,
        'movie-list.html',
        {'movies': movies, 'selected_category': category},
    )

@superuser_required
def updateMovie(request,movie_id):
    categories=Category.objects.all()
    movie=Movie.objects.get(id=movie_id)
    if request.method=="POST":
        movie_name=request.POST["movie"]
        tr_link=request.POST['trailer_link']
        cate=request.POST['category']
        re_date=request.POST['release_date']
        if "poster" in request.FILES:
            poster=request.FILES["poster"]
            movie.poster=poster
        desc=request.POST["description"]
        rating=request.POST["rating"]
        category=Category.objects.get(id=cate)
        movie.movie=movie_name
        movie.trailer_link=tr_link
        movie.release_date=re_date
        movie.description=desc
        movie.rating=rating
        movie.category=category
        movie.save()
        return redirect("movie_detail",movie_id)
    return render(request,"update-movie.html",{"movie":movie,"categories":categories})