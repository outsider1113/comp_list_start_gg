from django.shortcuts import render


from django.shortcuts import render
from django.http import HttpRequest
from datetime import datetime, timedelta

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from api.api import * 


def tournament_list(request: HttpRequest):
    selected_game = request.POST.get('game', 'Guilty Gear Strive')
    selected_location = request.POST.get('location', 'both')
    selected_date_str = request.POST.get('date', datetime.now().date().isoformat())

    # selected_date = datetime.fromisoformat(selected_date_str).date()
    # after_date = int(datetime.combine(selected_date, datetime.min.time()).timestamp())
    # before_date = after_date + 604800

    game_ids = {
        'Guilty Gear Strive': [411],
        'Tekken 8': [49783],
        'Street Fighter 6': [43868],
    }.get(selected_game, [])

    # placeholders

    data = start_tourneys()
    tournaments = []
    for i in data:
        tourn = {'name' : i['name'], 'startAt' : int(i['startAt']), 'isOnline' : True}
        tournaments.append(tourn)
    # tournaments = [
    #     {'name': 'Sample Tourney 1', 'startAt': 1753920000, 'isOnline': True},
    #     {'name': 'Sample Tourney 2', 'startAt': 1754006400, 'isOnline': False},
    # ]

    for t in tournaments:
        t['formatted_date'] = datetime.fromtimestamp(t['startAt']).strftime('%Y-%m-%d %H:%M')

    context = {
        'tournaments': tournaments,
        'selected_game': selected_game,
        'selected_location': selected_location,
        'selected_date': selected_date_str,
    }
    return render(request, 'main.html', context)