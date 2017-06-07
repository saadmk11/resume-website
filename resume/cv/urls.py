from django.conf.urls import url
from .views import *


urlpatterns = [
    # Examples:
    # url(r'^$', 'resume.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', home, name='home'),
    url(r'^create/', create, name='create'),
    url(r'^about/', about, name='about'),
    url(r'^(?P<username>\w+)/$', home, name='view_cv'),
    url(r'^(?P<username>\w+)/update/', update, name='update'),
]
