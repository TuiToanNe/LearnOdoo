from django.shortcuts import render

from django.http import HttpResponse
# get datetime
import datetime
 
# create a function
def geeks_view(request):
    # fetch date and time
    now = datetime.datetime.now()
    # convert to string
    html = "Time is {}".format(now)
    # return response
    return HttpResponse(html)
def viewBlog(q,blogname):
    html = "nameblog :" + blogname
    data = {
        "blogname" : blogname
    }
    return render(q, 'blog/blog.html', context=data)