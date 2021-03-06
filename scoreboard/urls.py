from django.urls import path

from . import views

app_name = 'scoreboard'
urlpatterns = [
    path('', views.index, name='index'),
    path('<str:competition_name>/', views.competition, name='competition'),
    path('<str:competition_name>/<str:participant_name>/detail', views.detail, name='detail'),
    path('<str:competition_name>/<str:participant_name>/log_exercise/<int:comp_exercise_id>', views.log_exercise, name='log_exercise'),
    path('<str:competition_name>/<str:participant_name>/log_pushups', views.log_pushups, name='log_pushups'),
    path('<str:competition_name>/<str:participant_name>/log_situps', views.log_situps, name='log_situps'),
    path('<str:competition_name>/<str:participant_name>/log_squats', views.log_squats, name='log_squats'),
    path('<str:competition_name>/<str:participant_name>/log_pullups', views.log_pullups, name='log_pullups'),
    path('<str:competition_name>/<str:participant_name>/log_dips', views.log_dips, name='log_dips'),

]