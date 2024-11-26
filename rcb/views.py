from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def virat(request):
    return HttpResponse('<h1>HARDHIK PANDHYA IS THE CAPTAIN OF MI</h1>')
def rcbteam(request):
    team='''
<h1><marquee>RCB SQUAD</marquee></h1>\n
<h2>VIRAT KOHLI(captain)</h2>\n
<h2>RAJAT PATIDAR</h2>\n
<h2>YASH DAYAL</h2>\n
<h2>LIAM LIVINGSTONE</h2>\n
<h2>PHIL SALT</h2>\n
<h2>JITESH SHARMA</h2>\n
<h2>RASIKH DAR</h2>\n
<h2>KRUNAL PANDYA</h2>\n
<h2>BHUVANESHWAR</h2>\n
<h2>TIM DAVID</h2>\n
<h2>JACOB</h2>\n'''
    return HttpResponse(team)