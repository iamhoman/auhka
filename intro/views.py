from django.shortcuts import render

def auhka(request):
    return render(request, 'intro/auhka.html')

def committee(request):
    return render(request, 'intro/committee.html')

def intro(request):
    return render(request, 'intro/intro.html')

def auhka_docs(request):
    return render(request, 'intro/auhka_docs.html')

