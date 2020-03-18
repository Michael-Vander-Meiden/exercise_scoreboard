from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('scoreboard/', include('scoreboard.urls')),
    path('admin/', admin.site.urls),
]