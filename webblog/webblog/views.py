from django.shortcuts import render

from django.http import HttpResponse
# get datetime
import datetime
 
# create a function
def home(request):
    # fetch date and time
    # convert to string
    html = "day la trang home"
    # return response
    return HttpResponse(html)