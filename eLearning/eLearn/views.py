from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def index(request):
    """The home page for eLearning"""
    return render(request, 'eLearn/index.html')

@login_required
def main(request):
    """The main page for eLearning"""
    return render(request, 'eLearn/main.html')
