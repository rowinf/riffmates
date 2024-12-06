from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# Create your views here.


def credits(request):
    content = "Nicky\n Your Name"
    return HttpResponse(content, content_type="text/plain")


def news(request):
    data = {
        "news": ["Riffmates now has a news page!@", "Riffmates has its first webpage"]
    }
    return render(request, "news.html", data)


def advanced_news(request):
    data = {
        "news": [
            (datetime.now(), "New Bands Lack Oompf, Say Critics"),
            (
                datetime.today(),
                "Megastars Are Beefing Yet Again, This is What We're Here For",
            ),
            (datetime.today(), "Metal Bands Stalking Fame's Shadow"),
        ]
    }
    return render(request, "news_adv.html", data)

def home(request):
    return render(request, "home.html")