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
    #get data to load main competition page
    competition = get_object_or_404(Competition, competition_name=competition_name)
    latest_participant_list = competition.participant_set.all()
    competition_exercise_list = competition.competitionexercise_set.all()
    participant_data = get_competition_data(latest_participant_list, competition_exercise_list)

    context = {'latest_scores_list': latest_participant_list,
                'top_participant_name': participant_data[0]['name'],
                'competition_exercise_list': competition_exercise_list,
                'participant_data': participant_data,
                'competition_name': competition_name}
    return render(request, 'scoreboard/index.html', context)

def get_competition_data(participant_list, competition_exercise_list):
    #TODO fill this out for the stuff you want on the front page
    #each participant's total score for each exercise
    competition_dump = []

    for participant in participant_list:
        participant_dict = {}
        participant_name = participant.participant_name
        participant_dict['name'] = participant_name
        scores_dict = get_compex_scores_for_participant(participant, competition_exercise_list)
        participant_dict.update(scores_dict)
        competition_dump.append(participant_dict)

    #TODO sort by total score, descending order
    competition_dump.sort(key=lambda item:item['total_score'], reverse=True)

    return competition_dump

def get_compex_scores_for_participant(participant, competition_exercise_list):
    scores_dict = {} 
    total_score = 0
    for i, comp_ex in enumerate(competition_exercise_list):
        #name
        exercise_name = comp_ex.exercise.exercise_name
        #score
        cur_participant_total = ExerciseVector.objects.filter(competition_exercise=comp_ex).filter(participant=participant).aggregate(Sum('delta'))['delta__sum']

        if not cur_participant_total:
            cur_participant_total=0

        scores_dict[exercise_name] = cur_participant_total
        #add this exercise to total score
        total_score += comp_ex.weight * cur_participant_total

    scores_dict["total_score"] = int(total_score)
    return scores_dict


        #TODO last week score 






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
