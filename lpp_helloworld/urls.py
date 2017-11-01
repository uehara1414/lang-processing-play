from django.conf.urls import url
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.contrib.staticfiles.views import serve
from . import views


urlpatterns = [
    url(r'^$', serve, kwargs={'path': 'lpp_helloworld/index.html'}),
    url(r'^(?P<path>.*\..*)$', RedirectView.as_view(url='/static/lpp_helloworld/%(path)s', permanent=False)),
    url(r'^api', views.index, name='index'),
]
urlpatterns += static('front', document_root='lpp_helloworld/front')
