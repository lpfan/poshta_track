from django.conf.urls import url
from rest_framework_mongoengine import routers as rfm_routers

from . import views


mongo_router = rfm_routers.SimpleRouter()
mongo_router.register(r'packages', views.PackageViewSet, base_name='package')

urlpatterns = [
    url(r'^parsel-status/(?P<parsel_code>\w+)$',
        views.ParselStatus.as_view(),
        name='parsel-status-detail'
        ),
]

urlpatterns += mongo_router.urls
