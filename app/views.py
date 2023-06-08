from django.shortcuts import render

# Create your views here.

def bootstrap_download(request):
    return render(request,'bootstrap_download.html')