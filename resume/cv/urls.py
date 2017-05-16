from django.conf.urls import url
from . import views


urlpatterns = [
    # Examples:
    # url(r'^$', 'resume.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^$/', ),zzz
    url(r'^$', views.details, name='details'),
    url(r'^create/', views.create, name='create'),
    url(r'^(?P<id>\d+)/update/', views.update, name='update'),
]