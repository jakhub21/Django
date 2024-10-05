from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse

monthly_challanges = {
    "january": "Work for 5h",
    "february": "Work for 8h",
    "march": "Learn Django for 20h",
    "april": "Work for 5h",
    "may": "Work for 8h",
    "june": "Learn Django for 20h",
    "july": "Work for 5h",
    "august": "Work for 8h",
    "september": "Learn Django for 20h",
    "october": "Work for 5h",
    "november": "Work for 8h",
    "december": None
}


# Create your views here.

def index(request):
    months = list(monthly_challanges.keys())
    
    return render(request, "challenges/index.html", {
        "months": months
    })


def monthly_challenge_by_number(request, month):
    months = list(monthly_challanges.keys())
    if month > len(months):
        return HttpResponseNotFound("<h1>Invalid month!</h1>")
    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challanges[month]
        return render(request, "challenges/challenge.html", {
            "month": month,
            "text": challenge_text
        })
    except:
        raise Http404()