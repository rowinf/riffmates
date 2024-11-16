from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def credits(request):
    content = "Nicky\n Your Name"
    return HttpResponse(content, content_type="text/plain")


def news(request):
    data = {
        "news": ["Riffmates now has a news page!@", "Riffmates has its first webpage"]
    }
    return render(request, "news.html", data)
