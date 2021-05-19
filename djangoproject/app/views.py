from django.contrib.sites import requests
from django.shortcuts import render
import requests
# Create your views here.


def index(request):
    url = "https://api.covid19india.org/data.json"

    data = requests.get(url).json()
    india = {
        'lastupdatedtime': data['statewise'][0]['lastupdatedtime'],
        'state': data['statewise'][0]['state'],
        'confirmed': data['statewise'][0]['confirmed'],
        'active': data['statewise'][0]['active'],
        'recovered': data['statewise'][0]['recovered'],
        'deaths': data['statewise'][0]['deaths'],
        'deltaconfirmed': data['statewise'][0]['deltaconfirmed'],
        'deltarecovered': data['statewise'][0]['deltarecovered'],
        'deltadeaths': data['statewise'][0]['deltadeaths'],
        'tested': data['tested'][-1]['totalsamplestested'],
        'testedasof': data['tested'][-1]['testedasof'],

    }
    list = []
    for i in range(37):
        payload = {
            'lastupdatedtime': data['statewise'][i]['lastupdatedtime'],
            'state': data['statewise'][i]['state'],
            'confirmed': data['statewise'][i]['confirmed'],
            'active': data['statewise'][i]['active'],
            'recovered': data['statewise'][i]['recovered'],
            'deaths': data['statewise'][i]['deaths'],
            'deltaconfirmed': data['statewise'][i]['deltaconfirmed'],
            'deltarecovered': data['statewise'][i]['deltarecovered'],
            'deltadeaths': data['statewise'][i]['deltadeaths'],
        }
        list.append(payload)
    return render(request, 'index.html', {'data': list, 'india':india})
