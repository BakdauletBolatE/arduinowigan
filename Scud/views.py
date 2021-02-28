from testd.models import Staff,StaffSessions
from django.http.response import HttpResponse
from django.shortcuts import render,get_object_or_404

def index(request):

    query = request.GET.get('rfid')


    try: 
        user = Staff.objects.get(uid=query)

        session = StaffSessions.objects.create(
            uid = query,
            check = 1
        )
        session.save()

        return HttpResponse(1) 
    except Staff.DoesNotExist: 
        session = StaffSessions.objects.create(
            uid = query,
            check = 0
        )
        session.save()
        return HttpResponse(0)

   

    
