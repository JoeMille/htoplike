from django.contrib import admin
from django.urls import path, include
from monitor import views as monitor_views

urlpatterns = [
    #admin
    path('admin/', admin.site.urls),

    #home
    path('', monitor_views.home, name='home'),

    #apis
    path('api/', include('monitor.urls'))
]