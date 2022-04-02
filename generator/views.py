import random
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')
    
    generated_password = ''
    
    length = int(request.GET.get('length'))
    uppercase = request.GET.get('uppercase')
    numbers = request.GET.get('numbers')
    special = request.GET.get('special')

    if uppercase:    
        characters.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    
    if numbers:    
        characters.extend('0123456789')
    
    if special:    
        characters.extend('@%+\/!#$^?:.(){}[]~_.')

    for char in range(length):
        generated_password += random.choice(characters)
        
    return render(request, 'password.html', {'password': generated_password})