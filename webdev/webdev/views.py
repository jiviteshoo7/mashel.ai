from django.shortcuts import render, redirect
from ai_assistant import get_response
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')


def mashel_ai(request):
    return render(request, 'mashel_ai.html')