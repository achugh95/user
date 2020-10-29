from django.urls import include, path
from user_assignment.users import views

urlpatterns = [
    path('', views.UserView.as_view())
]
