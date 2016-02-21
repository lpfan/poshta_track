from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^parsel-status/(?P<parsel_code>\w+)$',
        views.ParselStatus.as_view(),
        name='parsel-status-detail'
    ),
]
