from django.shortcuts import render
import datetime
# Create your views here.
def climate(request):
    date=datetime.datetime.now()
    msg=""
    image=''

    h=int(date.strftime('%H'))
    if h<12:
        msg="This is mornig time"
        image='morning'
    elif h<16:
        msg="This is afternoon time"
        image='afternoon'
    elif h<20:
        msg="This is evening time"
        image='evening'
    else:
        msg="This is night time"
        image='night'
    my_dict={'date':date,'message':msg,'image':image}

    return render(request,'climate.html',my_dict)
