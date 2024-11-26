from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def pat(request):
    return HttpResponse('<h1>PAT CUMMINS IS THE CAPTAIN OF CSK</h1>')
def srhteam(request):
    team='''
<h1><marquee>SRH SQUAD</marquee></h1>\n
<h2>PAT CUMMINS(captain)</h2>\n
<h2>HEINRICH KLASSEN(WK)</h2>\n
<h2>ABHISHEK S</h2>\n
<h2>TRAVIS HEAD</h2>\n
<h2>NITISH</h2>\n
<h2>SHAMI</h2>\n
<h2>HARSHAL PATEL</h2>\n
<h2>ISHAN KISHAN</h2>\n
<h2>RAHUL CHAHAR</h2>\n
<h2>ADAM ZAMPA</h2>\n
<h2>JAYDEV</h2>\n
<h2>KAMINDU</h2>\n
<h2>ESHAN MALINGA</h2>\n'''
    return HttpResponse(team)