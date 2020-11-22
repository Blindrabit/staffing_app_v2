from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions 
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title = 'Staffing APP API',
        default_version = 'v1',
        description = 'API for the staffing app',
        terms_of_service = 'https://www.google.com/policies/terms/',
        contact = openapi.Contact(email='a.r.tucker@hotmail.co.uk'),
        license = openapi.License(name='BSD License'),
    ),
    public=True,
    permission_classes = (permissions.AllowAny,),
)

urlpatterns = [
    #django admin 
    path('admin-not-admin-784512/', admin.site.urls),

    #User management
    path('accounts/', include('allauth.urls')),
    path('auth-api/', include('rest_framework.urls')),
    path('api/v1/dj-rest-auth/', include('dj_rest_auth.urls')),
    path('api/v1/dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),

    #Local apps
    path('', include('pages.urls')),
    path('calendar/', include('calendar_app.urls')),
    path('shifts/', include('shifts.urls')),
    path('api/v1/', include('api.urls')),
    path('', include('users.urls')),

    #api schema/doc's
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-uni'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
