from django.contrib import admin
from django.urls import path, include, re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^api/v1/user/', include('user_assignment.users.urls'))
]
