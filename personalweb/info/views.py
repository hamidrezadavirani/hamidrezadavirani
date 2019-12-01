from django.shortcuts import render

# Create your views here.
def home(request):
    context = {
        'posts': '',
    }
    return render(request, 'info/home.html', context)