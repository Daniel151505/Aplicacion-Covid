from django.shortcuts import render
import requests
import json

url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
    'x-rapidapi-key': "c01a2b41a5msh2047f72fbaa80dcp18d7a6jsne51475daddbe",
    'x-rapidapi-host': "covid-193.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers).json()


# Create your views here.
def helloworldview(request):
    context = {'response' : response}
    return render(request,'helloworld.html', context)
