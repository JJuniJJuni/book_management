from books import urls as books_urls
from django.conf.urls import include, url

from .views import HomePage, LoginView, LogoutView

urlpatterns = [
    url(r'^auth/', include('social_django.urls', namespace='social')),
    url(r'^$', LoginView.as_view(), name='login'),
    url(r'^logout$', LogoutView.as_view(), name='logout'),
    url(r'^home$', HomePage.as_view(), name='home_page'),
    url(r'^books/', include(books_urls)),
]
