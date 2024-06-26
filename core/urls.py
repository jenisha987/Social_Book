from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('settings/', views.settings, name="settings"),
    path('upload/', views.upload, name="upload"),
    path('like-post/<uuid:post_id>/', views.like_post, name="like-post"),
    path('profile/<str:username>/',  views.profile, name="profile"),
    path('search/', views.search, name="search"),
    path('follow/',  views.follow, name="follow"),
    path('signup/', views.signup, name="signup"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
]
