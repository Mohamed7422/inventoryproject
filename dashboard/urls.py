from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='dashboard-home'),
    path('recentActivity/',views.recentActivity,name='dashboard-recentActivity')
]