from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # urls.py from webapp 
    path('', include("webapp.urls")),
    path("__reload__/", include("django_browser_reload.urls")),
]
