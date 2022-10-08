from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    context = {}
    return render(request, 'base/home.html', context)

def solutions(request):
    context = {}
    return render(request, 'base/solutions.html', context)


def single_solutions(request, pk):
    next = ""

    if request.GET:
        next = request.GET['next']

    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        login(request, user)
        if next == "":
            return HttpResponseRedirect('home')
        else:
            return HttpResponseRedirect(next)

    context = {'id':pk}
    return render(request, 'base/single-solution.html', context)

def features(request):
    context = {}
    return render(request,'base/features.html', context)

def pricing(request):
    context = {}
    return render(request,'base/pricing.html', context)

def about(request):
    context = {}
    return render(request,'base/about.html', context)


def contact(request):
    context = {}
    return render(request,'base/contact.html', context)