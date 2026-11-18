from django.urls import path
from review import views

urlpatterns=[
    path("movie-review/",views.movie_list,name="review_movies"),
    path("add-review/<int:movie_id>/",views.add_review,name="add_review"),
    path("view-review/<int:movie_id>/",views.view_reviews,name="view_reviews"),
    path('edit/<int:review_id>/', views.edit_review, name='edit_review'),
    path('delete/<int:review_id>/', views.delete_review, name='delete_review'),
]