from re import T
from django.shortcuts import render
from .models import announcements , teams, teammembers, managers

# Create your views here.

def mainpage(request):

    announcement = announcements.objects.all()
    team = teams.objects.all()

    context = {
        'announcements': announcement,
        'teams': team
    }

    return render(request, 'pages/index.html', context)



def team(request, teamname):

    team = teams.objects.all()
    teamdesc = teams.objects.filter(teamname = teamname)
    teamnames = teams.objects.filter(teamname = teamname)

    for teamname in teamnames:
        teammember = teammembers.objects.filter(teamname = teamname.teamname)

    context = {
        'teams': team,
        'teammemberss': teammember,
        'teamdescribtion': teamdesc
    }

    return render(request, 'pages/teams.html', context)


def manager(request):

    team = teams.objects.all()
    manager = managers.objects.all().order_by('display')

    context = {
        'teams': team,
        'managers': manager
    }

    return render(request, 'pages/managers.html', context)


def sponsors(request):

    team = teams.objects.all()

    context = {
        'teams': team,
    }

    return render(request, 'pages/sponsors.html', context)


def achievements(request):
    
    team = teams.objects.all()

    context = {
        'teams': team,
    }

    return render(request, 'pages/achievements.html', context)


def events(request):
    team = teams.objects.all()

    context = {
        'teams': team,
    }

    return render(request, 'pages/events.html', context)