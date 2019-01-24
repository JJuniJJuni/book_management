from django.conf.urls import url

from .views import BookData
from .views import BookList

urlpatterns = [
    url(r'^$', BookList.as_view(), name='list'),
    url(r'^(?P<book_id>\d+)$', BookData.as_view(), name='info'),
]
