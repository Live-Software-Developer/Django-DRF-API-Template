from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('mainapp.urls')),
    path('api/auth/', include('customauth.urls')),
    path('api/account/', include('account.urls')),
]
