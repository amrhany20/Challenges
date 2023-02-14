from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse
#from django.template.loader import render_to_string

monthly_challanges = {
    "jan": "Do not eat meat for 30 days",
    "feb": "Train on django 20 minutes a day",
    "mar": "walt 30 mintes a day",
    "apr": "eat healthy",
    "may": "Drink water",
    "jun": "Read books",
    "jul": "swimming",
    "aug": "horse riding",
    "sep": "coding training",
    "oct": "eating konafa",
    "nov": "go to gym",
    "dec": None
}
# Create your views here.
def index(req):
    #list_items =""
    months = list(monthly_challanges.keys())
    return render(req,"challenges/index.html",{
         "months":months
    }) 
         #month_path = reverse("month_path",args=[month])
         #list_items+=f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"
    #response_data =f"<ul>{list_items}</ul>"

    #return HttpResponse(response_data)

def chall(req, month):
    try:
        chalText = monthly_challanges[month]
    except:
        return HttpResponseNotFound("<h1>this text is not a month supported format</h1>")
    return render(req,"challenges/challenge.html",{
         "text":chalText,"month":month
    })
    #respose_data = render_to_string("challenges/challenge.html")
    #f"<h1>{chalText}</h1>"
    #return HttpResponse(respose_data)

def challNum(req, month):
    months = list(monthly_challanges.keys())
    if month > len(months):
                return HttpResponseNotFound("this text is not a month supported format")
    redirected_month =months[month -1]
    redirected_path = reverse("month_path",args=[redirected_month])
    return HttpResponseRedirect(redirected_path)
