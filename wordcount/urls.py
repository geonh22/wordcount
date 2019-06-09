from django.contrib import admin
from django.urls import path
import app.views
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', app.views.home, name = 'home'),
    path('about/', app.views.about, name='about'),
    path('result/', app.views.result, name="result"),
]
