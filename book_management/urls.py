from django.conf.urls import include, url
from django.contrib import admin
from users import urls as users_url

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^users/', include(users_url)),
]
