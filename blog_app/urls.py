from blog_app import views
from django.urls import path


urlpatterns = [
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('home',views.home,name='home'),
    path('blogspage',views.blogspage,name='blogspage'),
    path('fillup',views.fillup,name='fillup'),
    path('specific/<int:pk>',views.specific,name='specific')

]