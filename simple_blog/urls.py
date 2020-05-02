from django.contrib import admin
from django.urls import path
from blogapp import views
urlpatterns = [

    path('', views.index),
    path('admin/', admin.site.urls),
    path('addblog/', views.createBlog)
]
