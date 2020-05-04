"""MusicRec URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url
from mv.views import mv_url,mv_detail,comment,video_url,video_detail

urlpatterns = [
    url(r'^mv-url/$',mv_url),
    url(r'^mv-detail/$',mv_detail),
    url(r'^comment/$',comment),
    url(r'^video-url/$',video_url),
    url(r'^video-detail/$',video_detail),
]
