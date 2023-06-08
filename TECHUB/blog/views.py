from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'blog/home.html')


def about(request):
    return render(request, 'blog/about.html')


def contact(request):
    return render(request, 'blog/contact.html')


def team(request):
    return render(request, 'blog/team.html')


def login(request):
    return render(request, 'blog/login.html')

def signup(request):
    return render(request, 'blog/sighup.html')


def profile(request):
    return render(request, 'blog/profile.html')


def register(request):
    return render(request, 'blog/register.html')


def test(request):
    return render(request, 'blog/test.html')


def update_profile(request):
    return render(request, 'blog/update_profile.html')


def update_address(request):
    return render(request, 'blog/update_address.html')


