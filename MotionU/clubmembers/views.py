from django.shortcuts import render

# Create your views here.
def members(request):
    return render(request, 'clubmembers/members.html')