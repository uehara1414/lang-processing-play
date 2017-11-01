from django.conf.urls import url
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.contrib.staticfiles.views import serve
from . import views


urlpatterns = [
    url(r'^api', views.index, name='index'),
]
