from django.http import HttpResponse
from django.shortcuts import render
import string 
    
punc = string.punctuation 

def index(request):
    return render(request,'index.html')



def analyze(request):

    dj_text = request.POST.get('text','default')
    removepunc = request.POST.get('removepunc','off')
    capfirst = request.POST.get('capfirst','off')
    newlineremove = request.POST.get('newlineremove','off')
    spaceremove = request.POST.get('spaceremove','off')
    analyzed = ""
    purpose = ""
    if removepunc == 'on':
        for char in dj_text:
            if char not in punc:
                analyzed = analyzed + char
        purpose = purpose + 'Removed Punctuation - '
        params = {'purpose':purpose,'analyzed_text':analyzed}
        dj_text = analyzed
        analyzed = ""
    if  capfirst == 'on':
        for char in dj_text:
            analyzed = analyzed + char.upper()
        purpose = purpose + 'Capitalize First - '
        params = {'purpose':purpose,'analyzed_text':analyzed}
        dj_text = analyzed
        analyzed = ""
    if  newlineremove == 'on':
        for char in dj_text:
            if char !="\n" and char !="\r":
                analyzed = analyzed + char
        purpose = purpose + 'New Line Remove - '
        params = {'purpose':purpose,'analyzed_text':analyzed}
        dj_text = analyzed
        analyzed = ""
    if  spaceremove == 'on':
        analyzed = dj_text.replace("  ", "")
        purpose = purpose+'Space Remove - '
        params = {'purpose':purpose,'analyzed_text':analyzed}
        dj_text = analyzed

    if (removepunc != 'on' and capfirst != 'on' and newlineremove != 'on' and spaceremove != 'on'):
        return HttpResponse ("Error")

    return render(request, 'analyze.html',params)

