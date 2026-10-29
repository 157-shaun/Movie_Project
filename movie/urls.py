from django.urls  import path
from movie import views

urlpatterns=[
    path("",views.home,name="index"),
    path("add-movie/",views.addMovie,name="add_movie"),
    path("movies/", views.movieList, name="movie_list"),
    path("movie-details/<int:id>/", views.movieDetails, name="movie_details"),
    path("delete-movie/<int:id>/", views.deleteMovie, name="delete_movie"),
    path("update-movie/<int:movie_id>/",views.updateMovie,name="edit_movie"),
]