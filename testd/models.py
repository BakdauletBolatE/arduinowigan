from django.db import models




class Staff(models.Model):

    uid = models.CharField('Uid человека',max_length=255)
    name = models.CharField('Name',max_length=255)

    def __str__(self):

        return self.name

    class Meta:
        verbose_name = "Работник"
        verbose_name_plural = "Работники"

class StaffSessions(models.Model):

    uid = models.CharField('Uid человека',max_length=255)
    check = models.BooleanField('Чек',default=0)

    def __str__(self):

        return self.uid
        
    class Meta:
        verbose_name = "Сессия"
        verbose_name_plural = "Сессий"