from django.db import models

from django.utils import timezone

class Spesilization(models.Model):

    name = models.CharField('Название специлизаций',max_length=255)


class Staff(models.Model):

    uid = models.CharField('Uid человека',max_length=255)
    name = models.CharField('Name',max_length=255)
    lastname = models.CharField('Username',default="LastName",max_length=255)
    spesilization = models.ForeignKey(Spesilization,blank=True,null=True,default=None,on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="ProfilePhotos/")

    def __str__(self):

        return self.name

    class Meta:
        verbose_name = "Работник"
        verbose_name_plural = "Работники"

class StaffSessions(models.Model):
    user = models.ForeignKey(Staff,blank=True,null=True,default=None,on_delete=models.CASCADE,related_name="session")
    uid = models.CharField('Uid человека',max_length=255)
    check = models.BooleanField('Чек',default=0)
    inout = models.CharField('Вход/Выход',max_length=255,default=0)
    created_at = models.DateTimeField('Время',default=timezone.now)

    def __str__(self):

        return self.uid
        
    class Meta:
        verbose_name = "Сессия"
        verbose_name_plural = "Сессий"