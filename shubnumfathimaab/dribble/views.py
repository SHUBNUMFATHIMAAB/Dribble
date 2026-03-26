from django.shortcuts import render

def dribble(request):
    return render(request, 'dribble.html')