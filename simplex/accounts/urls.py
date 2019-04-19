from django.urls import path

from . import views

# this is defined for namespace
# app_name = 'accounts'

# request mapping
urlpatterns = [
    path(r'', views.index, name='index'),
    path(r'results/', views.results, name='results'),
    path(r'detail/<int:uid>/', views.detail, name='detail'),
    path(r'signup', views.sign_up, name='sign up'),
    path(r'signin', views.sign_in, name='sign in'),
    path(r'verify', views.verify, name='verify'),
]