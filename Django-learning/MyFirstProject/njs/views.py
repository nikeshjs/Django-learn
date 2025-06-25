from django.shortcuts import render

# Create your views here.
def njs_app(request):
    return render(request, 'njs/app_njs.html')

