from django.shortcuts import render

from django.conf import settings

import xml.etree.ElementTree as ET

import os 

def home(request):
    game_servers = []
    for game_server in settings.GAME_SERVERS:
        if game_server['game'] == 'dst':
            query_result = os.popen('{} -a2s {}:{} -nh -xml -utf8 -htmlmode'.format(settings.QSTAT_COMMAND, game_server['host'], game_server['query_port'])).read()
            root = ET.fromstring(query_result)
            server = root[0]
            status = server.attrib['status']

        game_servers.append({
            'name': game_server['name'],
            'game_name': next((game for game in settings.GAMES if game['codename'] == game_server['game']))['name'],
            'game': game_server['game'],
            'host': game_server['host'],
            'port': game_server['port'],
            'status': status,
        })

    context = {
            'game_servers': game_servers,
        }
    return render(request, 'status/home.html', context)

def game(request, game):
    if game == 'dst':
        return render(request, 'status/games/dst.html')