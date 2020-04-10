from django.contrib import admin
from .models import Participant, Competition,  Exercise, CompetitionExercise, ExerciseVector

admin.site.register(Participant)
admin.site.register(Competition)
admin.site.register(Exercise)
admin.site.register(CompetitionExercise)
admin.site.register(ExerciseVector)

# Register your models here.
