from django.contrib import admin
from django.urls import path,include
from rest_framework.permissions import IsAdminUser
from dj_rest_auth.registration.views import RegisterView
urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/v1/", include("posts.urls")), # new
    path("api-auth/", include("rest_framework.urls")), # new
    path("api/v1/dj-rest-auth/", include("dj_rest_auth.urls")), # new
    path('api/v1/dj-rest-auth/registration/', RegisterView.as_view(permission_classes=[IsAdminUser])),
    path('accounts/', include('allauth.urls')),  # Incluye las URLs de allauth
 
    ] 