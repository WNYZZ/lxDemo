from django.db import models

# Create your models here.


class infoclass(models.Model):
    info_id = models.IntegerField(primary_key=True)
    info_type = models.IntegerField()
    is_check = models.BooleanField(False)
    is_Del = models.BooleanField(False)
    #order =
    sampling = models.IntegerField()
    correcting = models.IntegerField()
    town = models.IntegerField()
    enw_time = models.DateTimeField(auto_now_add=True)
    check_time = models.DateTimeField(auto_now=True)
    percent = models.FloatField(decimal_places=2)

    class Meta:
        db_table = "infoclass"
        ordering = ['-info_id']

