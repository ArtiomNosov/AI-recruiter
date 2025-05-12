from django.shortcuts import render





def home_page(request):
    return render(request, 'home/index.html')

def use_cases(request):
    return render(request, 'home/use_cases.html')

def resources(request):
    return render(request, 'home/resources.html')

