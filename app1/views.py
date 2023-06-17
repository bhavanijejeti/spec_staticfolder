from django.shortcuts import render

# Create your views here.
def specstatic(request):
    return render(request,'specstatic.html')