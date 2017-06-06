from django.conf.urls import url
from . import views


urlpatterns = [
    # Examples:
    # url(r'^$', 'resume.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^$/', ),
    url(r'^$', views.home, name='home'),
    url(r'^create/', views.create, name='create'),
    url(r'^about/', views.about, name='about'),
    url(r'^(?P<username>\w+)/$', views.home, name='view_cv'),
    url(r'^(?P<username>\w+)/update/', views.update, name='update'),
]