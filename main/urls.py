"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from facebook.views import play, play2, profile
from facebook.views import newsfeed, detail_feed
from facebook.views import pages
from facebook.views import remove_feed

from facebook.views import new_feed, edit_feed, fail

from facebook.views import new_page

from facebook.views import remove_page, edit_page

urlpatterns = [
    path('admin/', admin.site.urls),

    path('play/', play),

    path('play2/', play2),

    path('testguy/profile/', profile),

    path('', newsfeed),

    # path('feed/<pk>/', detail_feed),
    path('pages/', pages),

    path('new/', new_feed),

    path('feed/<pk>/', detail_feed),
    path('feed/<pk>/remove/', remove_feed),
    path('feed/<pk>/edit/', edit_feed),

    path('fail/', fail),

    path('pages/new/', new_page),

    path('pages/remove/', remove_page),
    path('pages/edit/', edit_page)

]
