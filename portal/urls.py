from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('admin-home/', views.admin_home, name='admin_home'),
    path('user/', views.user_home, name='user_home'),
    path('find-jobs/', views.find_jobs, name='find_jobs'),
    path('apply-job/<int:job_id>/', views.apply_job, name='apply_job'),
    path('profile/', views.profile, name='profile'),
    path('applied-jobs/', views.applied_jobs, name='applied_jobs'),
    path('help/', views.help_page, name='help'),
    path('company/', views.company, name='company'),
    path('post-job/', views.post_job, name='post_job'),
    path('view-applications/', views.view_applications, name='view_applications'),
    path('schedule-interview/', views.schedule_interview, name='schedule_interview'),
    path('logout/', views.logout, name='logout'),
]
