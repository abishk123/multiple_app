from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def ruturaj(request):
    return HttpResponse('<h1>RUTHURAJ IS THE CAPTAIN OF CSK</h1>')
def cskteam(request):
    team='''
<h1><marquee>CSK SQUAD</marquee></h1>\n
<h2>RUTHURAJ(captain)</h2>\n
<h2>MS.DHONI(WK)</h2>\n
<h2>M.PATHIRANA</h2>\n
<h2>SHIVAM DUBE</h2>\n
<h2>DEVON CONWAY</h2>\n
<h2>R TRIPATHI</h2>\n
<h2>R RAVINDRA</h2>\n
<h2>R ASHWIN</h2>\n
<h2>VIJAY SHANKAR</h2>\n
<h2>NOOR</h2>\n
<h2>KHALEEL</h2>\n
<h2>SAM CURRAN</h2>\n
<h2>DEEPAK HOODA</h2>\n'''
    return HttpResponse(team)
