from django.shortcuts import render
from django.http import HttpResponse,Http404

# Create your views here.
def index(request):
    return render(request,"singlepage/index.html")
texts=[" hi this is a website created by django framework",
        " this is our 2nd page of django framework",
         " this is our 3rd page of django framework and the last one"]
def section(request,num):
    if 1<= num <=3:
        return HttpResponse(texts[num-1])
    else:
        raise Http404("No such section")
