from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
 #convert to string


# Create your views here.

monthly_challenges = {
    "january" : "Drink water everyday!",
    "february": "Stay fit",
    "march" : None,
    "april" : "Go out",
    "may" : "read a book",
    "june": "Drink tea",
    "july": "challenge yourself",
    "august" :"listen to music!",
    "september" : "go hiking every week",
    "october" : "rest when you need ",
    "november" : "take a deep breath and relax",
    "december" : "be consistent in your path"
}

def monthly_challenge_by_number(request, month):
    months  = list(monthly_challenges.keys())
    if month > len(months) :
        return HttpResponseNotFound("invalid month")
    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge-str", args = [redirect_month])
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        #monthly_challenges.keys()
        return render(request, "challenges/challenge.html", 
        context = {
            "text" : challenge_text,
            "month_name" : month
        })

        
    except:
    
        raise Http404()

    
    

def index(request):
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {
        "list_of_months": months
    })
        
  


    



    #return response to the browser sending request(client)
    #request = a parameter passed in automatically when the function is executed