from django.shortcuts import render, get_object_or_404 
from django.http import HttpResponse
from roster.models import Player, Sport, Team
import json
import pdb

# Create your views here.
def home(request):
    return render(request, "sports.html", {
        'sports': Sport.objects.all(),
        'teams': Team.objects.all(),
        'players': Player.objects.all()
    })

def teams(request, pk):
    sport = get_object_or_404(Sport, id=pk)
    return render(request, "teams.html", {
        'teams': sport.teams.all(),
        'sport': sport
    })

def roster(request, pk):
    team = get_object_or_404(Team, id=pk)
    players = team.players.all()
    player_geodata = []
    for player in players:
        name = "%s %s" %(player.first, player.last)
        address = "%s, %s" %(player.city, player.state)
        player_geodata.append({"name": name, "address": address})
    return render(request, "roster.html", {
        'team': team,
        'players': players,
        'player_geodata': json.dumps(player_geodata),
    })

def player(request, pk):
    player = get_object_or_404(Player, id=pk)
    return render(request, "player.html", {
        'player': player
    })

def teams_all(request):
    return render(request, "teams_all.html", {
        'teams': Team.objects.all()
    })
def players_all(request):
    return render(request, "players_all.html", {
        'players': Player.objects.all()
    })
