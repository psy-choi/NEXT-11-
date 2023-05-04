from django.urls import path
from loginapp	import views
app_name = 'loginapp'
urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path("login/", views.login, name="login"),
    path('', views.home, name='home'),
]