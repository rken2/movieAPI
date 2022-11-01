from django.urls import path

from . import views

urlpatterns = [
    path('', views.getMovies),
    path('<int:year>', views.getMovieByYear),
    path('add', views.addMovie),
    path('update', views.updateMovie),
    path('delete/<str:title>', views.deleteMovie),
]