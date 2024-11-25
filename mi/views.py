from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def captain(request):
    return HttpResponse('<h1>HARDHIK PANDHYA IS THE CAPTAIN OF MI</h1>')
def miteam(request):
    team='''
<h1>MI SQUAD</h1>\n
<h2>H.PANDHYA(captain)</h2>\n
<h2>ISHAN KISHAN(WK)</h2>\n
<h2>ROHITH SHARMA</h2>\n
<h2>BHUMRA</h2>\n
<h2>SURYA KUMAR YADAV</h2>\n
<h2>TEEKSHANA</h2>\n
<h2>CONVOY</h2>\n'''
    return HttpResponse(team)
