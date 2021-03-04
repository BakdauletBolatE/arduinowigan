
from django.contrib import admin
from django.urls import path,include
from .views import index,send,allStaff,questions,detailStaff,indexJson
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',index,name="index"),
    path('allstaff/',allStaff,name="allStaff"),
    path('questions/',questions,name="questions"),
    path('staff/<int:id>',detailStaff,name="detailStaff"),
    path('send/',send),
    path('admin/', admin.site.urls),
]

urlpatterns += [
    path('api/',indexJson,name="indexJson"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)