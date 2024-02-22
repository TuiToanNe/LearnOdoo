from django.shortcuts import render

from django.http import HttpResponse
# get datetime
 
# create a function
def Name(request):

    # convert to string
    html = "Nguyen Ngoc Phuc Toan"
    # return response
    return HttpResponse(html)

def viewProfile(q,name):
    html = "name :" + name
    data = {
        "name" : name
    }
    return render(q, 'Profile/profile.html', context=data)
