from django.conf.urls import url, include
from django.urls import path
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'service', views.ServiceViewSet)
router.register(r'customer', views.CustomerViewSet)
router.register(r'worker', views.WorkerViewSet)
router.register(r'review', views.ReviewViewSet)

urlpatterns = [
    path('', views.cat.as_view()),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/', include(router.urls)),
    url(r'^home/$', views.cat.as_view(), name='home'),
    path('creSer', views.creSer.as_view()),
    url(r'creUser/$', views.UserFormView.as_view(), name='creUser'),
    path('review', views.reView.as_view()),
    path('services', views.vewSer.as_view()),
    path('getCatSer', views.getCategoryServices.as_view()),
    path('getSer', views.getService.as_view()),
    path('write', views.writeView.as_view()),
    path('viz', views.vizView.as_view()),
]