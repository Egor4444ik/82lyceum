from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from account import views
from account import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
]