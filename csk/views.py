from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def captain(request):
    return HttpResponse('<h1>RUTHURAJ IS THE CAPTAIN OF CSK</h1>')
def cskteam(request):
    team='''
<h1>CSK SQUAD</h1>\n
<h2>RUTHURAJ(captain)</h2>\n
<h2>MS.DHONI(WK)</h2>\n
<h2>PATHIRANA</h2>\n
<h2>CHAHAL</h2>\n
<h2>NATARAJAN</h2>\n
<h2>TEEKSHANA</h2>\n
<h2>CONVOY</h2>\n'''
    return HttpResponse(team)
