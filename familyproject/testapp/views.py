from django.shortcuts import render

# Create your views here.
def family(request):
    return render(request,'testapp/family.html')