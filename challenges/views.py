from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse,HttpResponseNotFound, HttpResponseRedirect

# Create your views here.

my_challenges = {
    "janurary":"This is JANURARY",
    "feburary":"This is FEBURARY",
    "march":"This is MARCH",
    "april":"This is APRIL",
    "may":"This is MAY",
    "june":"This is JUNE",
    "july":"This is JULY",
    "august":"This is AUGUST",
    "september":"This is SEPTEMBER",
    "october":"This is OCTOBER",
    "november":"This is NOVEMBER",
    "december":"This is DECEMBER"
}

def index(request):
    list_items = ""
    months = list(my_challenges.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("monthly", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"

    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)

# def monthly_challenge_by_number(request,month):
#     months = list(my_challenges.keys())
#     if month > len(my_challenges):
#         return HttpResponseNotFound("Invalid Month")
#     redirect_month =  months[month-1]
#     return HttpResponse(my_challenges[redirect_month])        

def monthly_challenge_by_number(request, month):
    months = list(my_challenges.keys())
    if month > len(my_challenges):
        return HttpResponseNotFound("Invalid Month")
    redirect_month = months[month-1]
    return HttpResponseRedirect("/challenges/"+redirect_month)


def monthly_challenge(request, month):
    try:
        challenge = my_challenges[month]
        response = f"<h1>{challenge}</h1>"
        return HttpResponse(response)
    except:
        return HttpResponseNotFound("<h1>This month is not supported</h1>")
