from django.conf.urls import url
from . import views


urlpatterns = [
    # Examples:
    # url(r'^$', 'resume.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^$/', ),
    url(r'^$', views.details, name='details'),
    url(r'^create/', views.create, name='create'),
    url(r'^(?P<username>\w+)/$', views.view_cv, name='view_cv'),
    url(r'^(?P<username>\w+)/update/', views.update, name='update'),
]