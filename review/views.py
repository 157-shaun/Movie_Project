
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from movie.models import Movie
from .models import Review


@login_required(login_url="login")
def movie_list(request):
    movies = Movie.objects.all()
    return render(request, "movie-reviews.html", {
        "movies": movies
    })


@login_required(login_url="login")
def add_review(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    

    # Check whether this user has already reviewed this movie
    existing_review = Review.objects.filter(
        user=request.user,
        movie=movie
    ).first()

    if existing_review:
        return redirect("view_reviews", movie_id=movie.id)

    if request.method == "POST":
        review_text = request.POST.get("review")

        if review_text:
            Review.objects.create(
                user=request.user,
                movie=movie,
                review=review_text
            )

        return redirect("view_reviews", movie_id=movie.id)

    return render(request, "add-reviews.html", {
        "movie": movie
    })


@login_required(login_url="login")
def view_reviews(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)

    reviews = Review.objects.filter(movie=movie).order_by("-date")
    

    my_review = Review.objects.filter(
        movie=movie,
        user=request.user
    ).first()

    return render(request, "view-reviews.html", {
        "movie": movie,
        "reviews": reviews,
        "my_review": my_review
    })


@login_required(login_url="login")
def edit_review(request, review_id):
    review = get_object_or_404(
        Review,
        id=review_id,
        user=request.user
    )

    if request.method == "POST":
        review_text = request.POST.get("review")

        if review_text:
            review.review = review_text
            review.save()

        return redirect("view_reviews", movie_id=review.movie.id)

    return render(request, "edit-review.html", {
        "review": review
    })


@login_required(login_url="login")
def delete_review(request, review_id):
    review = get_object_or_404(
        Review,
        id=review_id,
        user=request.user
    )

    movie_id = review.movie.id

    if request.method == "POST":
        review.delete()
        return redirect("view_reviews", movie_id=movie_id)

    return redirect("view_reviews", movie_id=movie_id)
