from django.shortcuts import render

# Create your views here.
def healthcare(request):
    return render(request,'health.html')