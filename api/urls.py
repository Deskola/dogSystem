from django.urls import path, include

from . import views

urlpatterns = [
    path('dogs', views.ListOfDogs.as_view()),
    path('dogs/<int:pk>/', views.DetailOfDog.as_view()),
    path('medications', views.ListOfMedication.as_view()),
    path('medications/<int:pk>/', views.DetailOfMedication.as_view()),
    path('feeds', views.ListOfFeed.as_view()),
    path('feeds/<int:pk>/', views.DetailOfFeed.as_view()),
    path('reviews', views.ListOfReview.as_view()),
    path('reviews/<int:pk>/', views.DetailOfReview.as_view()),
    path('users', views.ListOfDogs.as_view()),
    path('users/<int:pk>/', views.DetailOfDog.as_view()),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls'))

]