from testd.models import Staff,StaffSessions
from django.http.response import HttpResponse
from django.shortcuts import render,get_object_or_404

def index(request):

    queryin = request.GET.get('rfidin')
    queryout = request.GET.get('rfidout')
    if queryout:

        try:
            user = Staff.objects.get(uid=queryout)

            session = StaffSessions.objects.create(
                uid = queryout,
                check = 1
            )
            session.save()

            return HttpResponse(str(1) +"out")
        except Staff.DoesNotExist:
            session = StaffSessions.objects.create(
                uid = queryout,
                check = 0
            )
            session.save()
            return HttpResponse(str(0)+"out")
    elif queryin:

        try:
            user = Staff.objects.get(uid=queryin)

            session = StaffSessions.objects.create(
                uid=queryin,
                check=1
            )
            session.save()

            return HttpResponse(str(1) + "in")
        except Staff.DoesNotExist:
            session = StaffSessions.objects.create(
                uid=queryin,
                check=0
            )
            session.save()
            return HttpResponse(str(0)+'in')
    else:
        return HttpResponse("nothing")
    
