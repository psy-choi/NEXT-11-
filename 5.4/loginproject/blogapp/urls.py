from django.urls import path
from blogapp import views
app_name = 'blogapp'
urlpatterns = [
    path('home', views.home, name='home'),
    path("logout/", views.logout, name="logout"),
    path('new/', views.new, name='new'),
    path('detail/<int:post_pk>', views.detail, name='detail'),
    path('edit/<int:post_pk>', views.edit, name='edit'),
    path('delete/<int:post_pk>', views.delete, name='delete'),
    path('delete-comment/<int:post_pk>/<int:comment_pk>', views.delete_comment, name='delete_comment'),

]