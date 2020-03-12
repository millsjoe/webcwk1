from django.urls import path, include
from api import views
from rest_framework import routers
from django.views.decorators.csrf import csrf_exempt


router = routers.DefaultRouter()

# router.register(r'groups', views.GroupViewSet)
router.register(r'lecturer', views.LecturerViewSet)
router.register(r'modules', views.ModuleViewAll)
router.register(r'ratings', views.ListRatings)

app_name = 'api'
urlpatterns = [
    path('register', csrf_exempt(views.RegisterUser.as_view())),
    path('', include(router.urls)),
    path('auth/', include('rest_auth.urls')),
    path('average', views.LecturerModuleRating.as_view()),
    path('view', views.AverageAllRatings.as_view()),
    path('rate/', views.GiveRating.as_view())


]