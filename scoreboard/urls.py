from django.urls import path

from . import views

app_name = 'scoreboard'
urlpatterns = [
    path('', views.index, name='index'),
    path('<str:participant_name>/detail', views.detail, name='detail'),
    path('<str:participant_name>/log_pushups', views.log_pushups, name='log_pushups'),
    path('<str:participant_name>/log_situps', views.log_situps, name='log_situps'),
    path('<str:participant_name>/log_squats', views.log_squats, name='log_squats'),
    path('<str:participant_name>/log_pullups', views.log_pullups, name='log_pullups'),
    path('<str:participant_name>/log_dips', views.log_dips, name='log_dips'),

]