from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from netapp import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'movies', views.MoviesViewSet)
router.register(r'movies2', views.MoviesViewSet2)
router.register(r'film', views.MoviesViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]