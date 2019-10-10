from django.conf.urls import include
from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from rest_framework.routers import SimpleRouter

router = SimpleRouter()

urlpatterns = [
    path('login/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('registration/', include('rest_registration.api.urls')),
]

urlpatterns += router.urls
