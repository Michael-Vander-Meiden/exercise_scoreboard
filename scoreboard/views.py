from django.db.models import Sum
from django.shortcuts import render, get_object_or_404
from django.template import  loader
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Participant, Competition, CompetitionExercise, Exercise, ExerciseVector

import json

def index(request):
    latest_scores_list = Participant.objects.order_by('-total_score')
    context = {'latest_scores_list': latest_scores_list,
                'top_participant': latest_scores_list[0]}
    return render(request, 'scoreboard/index.html', context)

def competition(request, competition_name, ):
    competition = get_object_or_404(Competition, competition_name=competition_name)
    latest_participant_list = competition.participant_set.all().order_by('-total_score')
    
    context = {'latest_scores_list': latest_scores_list,
                'top_participant': latest_scores_list[0]}
    return render(request, 'scoreboard/index.html', context)

def get_competition_data(participant_list):
    #TODO fill this out for the stuff you want on the front page
    competition_dump = []



def detail(request, competition_name, participant_name):
    participant = get_object_or_404(Participant, participant_name=participant_name)
    comp_exercise_list = CompetitionExercise.objects.filter(competition__competition_name=competition_name)
    
    #get relevant stats
    data = get_detail_data(participant, comp_exercise_list)

    context = {'participant': participant,
               'comp_exercise_list': comp_exercise_list,
               'data': data}
    return render(request, 'scoreboard/detail.html', context)

def get_detail_data(participant, comp_exercise_list):
    # we are trying to build a json packet that has everything needed for detail to render it's page
    details_dump = {}

    #all-time stats
    for i,comp_ex in enumerate(comp_exercise_list):
        #initate current dictionary
        cur_dict = {}
        
        #add comp_exercise object
        cur_dict['comp_exercise'] = comp_ex

        #add id
        cur_dict['comp_ex_id'] = comp_ex.id

        #add name
        cur_exercise_name = comp_ex.exercise.exercise_name
        cur_dict['comp_exercise_name'] = cur_exercise_name 

        #add total
        cur_participant_total = ExerciseVector.objects.filter(competition_exercise=comp_ex).filter(participant=participant).aggregate(Sum('delta'))['delta__sum']
        cur_dict['exercise_score'] = cur_participant_total

        #add everything to thing
        details_dump[i] = cur_dict

    #json_packet = json.dumps(all_time)
    return details_dump



def log_exercise(request, competition_name, participant_name, comp_exercise_id):
    participant = get_object_or_404(Participant, participant_name=participant_name)
    comp_exercise = get_object_or_404(CompetitionExercise, pk=comp_exercise_id)
    #TODO change index variable to delta
    delta = int(request.POST['quantity'])
    
    # create exercise vector TODO: add stuff
    exercise_vec = ExerciseVector.objects.create(delta=delta, participant=participant, competition_exercise=comp_exercise)

    context = {'participant': participant}
    return HttpResponseRedirect(reverse('scoreboard:competition', args=[competition_name]))


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
