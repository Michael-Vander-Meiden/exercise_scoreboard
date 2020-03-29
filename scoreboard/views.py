from django.shortcuts import render, get_object_or_404
from django.template import  loader
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Participant, Competition

def index(request):
    latest_scores_list = Participant.objects.order_by('-total_score')
    context = {'latest_scores_list': latest_scores_list,
    			'top_participant': latest_scores_list[0]}
    return render(request, 'scoreboard/index.html', context)

def competition(request, competition_name, ):
    competition = get_object_or_404(Competition, competition_name=competition_name)
    latest_scores_list = competition.participant_set.all().order_by('-total_score')
    context = {'latest_scores_list': latest_scores_list,
    			'top_participant': latest_scores_list[0]}
    return render(request, 'scoreboard/index.html', context)

def detail(request, competition_name, participant_name):
	participant = get_object_or_404(Participant, participant_name=participant_name)
	context = {'participant': participant}
	return render(request, 'scoreboard/detail.html', context)


def log_pushups(request, competition_name, participant_name):
	participant = get_object_or_404(Participant, participant_name=participant_name)
	quantity = int(request.POST['quantity'])
	participant.score += quantity
	participant.save()
	context = {'participant': participant}
	return HttpResponseRedirect(reverse('scoreboard:competition', args=[competition_name]))

def log_situps(request, competition_name, participant_name):
	participant = get_object_or_404(Participant, participant_name=participant_name)
	quantity = int(request.POST['quantity'])
	participant.situps_count += quantity
	participant.save()
	context = {'participant': participant}
	return HttpResponseRedirect(reverse('scoreboard:competition', args=[competition_name]))

def log_squats(request, competition_name, participant_name):
	participant = get_object_or_404(Participant, participant_name=participant_name)
	quantity = int(request.POST['quantity'])
	participant.squats_count += quantity
	participant.save()
	context = {'participant': participant}
	return HttpResponseRedirect(reverse('scoreboard:competition', args=[competition_name]))

def log_pullups(request, competition_name, participant_name):
	participant = get_object_or_404(Participant, participant_name=participant_name)
	quantity = int(request.POST['quantity'])
	participant.pullups_count += quantity
	participant.save()
	context = {'participant': participant}
	return HttpResponseRedirect(reverse('scoreboard:competition', args=[competition_name]))

def log_dips(request, competition_name, participant_name):
	participant = get_object_or_404(Participant, participant_name=participant_name)
	quantity = int(request.POST['quantity'])
	participant.dips_count += quantity
	participant.save()
	context = {'participant': participant}
	return HttpResponseRedirect(reverse('scoreboard:competition', args=[competition_name]))
