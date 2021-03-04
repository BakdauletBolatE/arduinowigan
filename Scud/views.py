from testd.models import Staff,StaffSessions
from django.http.response import HttpResponse,JsonResponse
from django.shortcuts import render,get_object_or_404
from django.core import serializers

import datetime
date = datetime.date.today()
day = date.strftime("%d")
month = date.strftime("%B")


def allStaff(request):
    sessions = StaffSessions.objects.exclude(user=None)
    data = {
        "sessions":sessions,
        "date":date
    }

    return render(request,'main/allStaff.html',data)

def questions(request):
    sessions = StaffSessions.objects.filter(user=None)
    data = {
        "sessions":sessions,
        "date":date,
        
    }

    return render(request,'main/questions.html',data)

def detailStaff(request,id):

    staff = Staff.objects.get(id=id)
    sessions = staff.session.all()
    data = {
        "sessions":sessions,
        "date":date,
        'staff':staff
    }

    return render(request,'main/detail.html',data)


def index(request):

    sessions = StaffSessions.objects.filter(created_at__day=day).order_by('-created_at')

    data = {
        "sessions":sessions,
        "date":date
    }

    return render(request,'main/main.html',data)

def indexJson(request):
    session = StaffSessions.objects.last()
    if session.user == None:
        user = "None"
    else:
        user = list(Staff.objects.values_list().get(id=session.user_id))


    sessions = list(StaffSessions.objects.values_list().last())

    return JsonResponse({'data':sessions,'user':user})



def send(request):

    queryin = request.GET.get('rfidin')
    queryout = request.GET.get('rfidout')
    if queryout:

        try:
            user = Staff.objects.get(uid=queryout)

            session = StaffSessions.objects.create(
                uid = queryout,
                check = 1,
                inout="Шықты",
                user=user
            )
            session.save()

            return HttpResponse(str(1))
        except Staff.DoesNotExist:
            session = StaffSessions.objects.create(
                uid = queryout,
                check = 0,
                inout="Шықты"
            )
            session.save()
            return HttpResponse(str(0))
    elif queryin:

        try:
            user = Staff.objects.get(uid=queryin)

            session = StaffSessions.objects.create(
                uid=queryin,
                check=1,
                inout="Кірді",
                user=user
            )
            session.save()

            return HttpResponse(str(1))
        except Staff.DoesNotExist:
            session = StaffSessions.objects.create(
                uid=queryin,
                check=0,
                inout="Кірді"
            )
            session.save()
            return HttpResponse(str(0))
    else:
        return HttpResponse("nothing")
    
