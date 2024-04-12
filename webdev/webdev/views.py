from django.shortcuts import render, redirect
from django.http import JsonResponse
import openai
from django.contrib import auth
from django.contrib.auth.models import User
from .models import Chat
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt


def index(request):
    return render(request, 'index.html')

def mashel_ai(request):
    return render(request, 'mashel_ai.html')

openai_api_key = ''
openai.api_key = openai_api_key

def ask_openai(message):
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo-0125",
        messages=[
            {"role": "system", "content": "You are an helpful assistant."},
            {"role": "user", "content": message},
        ]
    )
    answer = response.choices[0].message.content.strip()
    return answer

def mashel_ai(request):
    chats = Chat.objects.filter(user=request.user)

    if request.method == 'POST':
        message = request.POST.get('message')
        response = ask_openai(message)

        chat = Chat(user=request.user, message=message, response=response, created_at=timezone.now())
        chat.save()
        return JsonResponse({'message': message, 'response': response})
    
    return render(request, 'mashel_ai.html', {'chats': chats})

def get_data(request):
    if request.method == 'POST':
        # Process the POST request data
        msg = request.POST.get('msg')
        
        # Perform some logic or call a function to generate a response
        response_data = ask_openai(msg)
        
        # Return the response as JSON
        return JsonResponse({'response': response_data})