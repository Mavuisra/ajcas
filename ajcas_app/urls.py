from django.urls import path
from . import views

app_name = "ajcas_app"
urlpatterns = [
    path('', views.index, name='home'),
    path('article', views.article_list, name='article_list'),
    path('article/<int:pk>/', views.article_detail, name='article_detail'),
    path('article/<int:pk>/like/', views.like_article, name='like_article'),
    path('adhesion/', views.membership_form, name='membership_form'),
    path('success/', views.form_success, name='form_success'),
    path('login/', views.loginpage, name = 'login'),
    path('logout/', views.logoutpage, name = 'logout'),
    path('profile-member/', views.profile, name = 'profile-member'),

]
