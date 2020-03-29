from django.db import models

# Create your models here.

class Competition(models.Model):
	competition_name = models.CharField(max_length=200)





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