"""GroupBloger URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from blog import views as blog_views
from blog.views import test, post_list, post_detail, no_path, new_post
from settings import MEDIA_ROOT


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', no_path),
    url(r'^test/', test),
    url(r'^blog/$', post_list),
    url(r'^blog/(?P<id>\d+)/$', post_detail),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root':MEDIA_ROOT}),
    url(r'^post/new/$', new_post, name='new_post'),

]
