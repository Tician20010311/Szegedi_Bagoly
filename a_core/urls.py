from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from a_users.views import profile_view
from a_home.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('news/', news, name="news"),
    path('without_border/', without_border, name="without_border"),
    path('about/', about, name="about"),
    path('digital/', digital, name="digital"),
    path('enroll/', enroll, name="enroll"),
    path('accounts/', include('allauth.urls')),
    path('', home_view , name="home"),
    path('profile/', include('a_users.urls')),
    path('@<username>/', profile_view, name="profile"),

    path('firstday/', dayone, name="dayone"),
    path('secondday/', daytwo, name="daytwo"),
    path('thirdday/', daythree, name="daythree"),
    path('fouthday/', dayfour, name="dayfour"),
    path('fiftday/', dayfive, name="dayfive"),
]

# Only used when DEBUG=True, whitenoise can serve files when DEBUG=False
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
