from django.db import models

# Create your models here.

class Competition(models.Model):
	competition_name = models.CharField(max_length=200)

	#return comp name
	def __str__(self):
		return self.competition_name

class Participant(models.Model):
	competition = models.ForeignKey(Competition, on_delete=models.CASCADE, null=True, blank=True)
	participant_name = models.CharField(max_length=200)

	#score is actually pushups
	score = models.IntegerField(default=0)
	situps_count = models.IntegerField(default=0)
	squats_count = models.IntegerField(default=0)
	pullups_count = models.IntegerField(default=0)
	dips_count = models.IntegerField(default=0)

	#total score is sum of all other stuff
	total_score = models.IntegerField(default=0)

	def __str__(self):
		return self.participant_name

	def save(self, *args, **kwargs):
		self.total_score = ((self.score*.45) + (self.situps_count*0.3) + 
						   (self.squats_count*.25) + (self.pullups_count*.45) +
						   (self.dips_count*.45))
		super(Participant, self).save(*args, **kwargs) #this is the real save

# Exercise class defines the characteristics of an exercise for use in competitions
class Exercise(models.Model):
	#Name of the exercise
	exercise_name = models.CharField(max_length=200)

	#The name of the units value (miles, pushups, seconds, "")
	units = models.CharField(max_length=100)

	#True if time will be used
	is_time = models.BooleanField(default=False)

#This class is made to be intantiated to link exercise models to each competition
class CompetitionExercise(models.Model):
	#TODO override save with exercise name feature
	exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
	competition = models.ForeignKey(Competition, on_delete=models.CASCADE)
	name = models.CharField(max_length=200, default="")
	weight = models.FloatField(default=1)

	def save(self, *args, **kwargs):
		self.name = self.exercise.exercise_name
		super(CompetitionExercise, self).save(*args, **kwargs) #this is the real save


# This class records changes in a participants count for a specific exercise
class ExerciseVector(models.Model):
	#The actual change
	delta = models.IntegerField(default=0)

	created_on = models.DateTimeField(auto_now_add=True)

	participant = models.ForeignKey(Participant, on_delete=models.CASCADE)

	competition_exercise = models.ForeignKey(CompetitionExercise, on_delete=models.CASCADE)