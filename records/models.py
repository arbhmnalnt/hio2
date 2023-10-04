from django.db import models

# Create your models here.

class TimeStampMixin(models.Model):
    created_at      = models.DateTimeField(auto_now_add=True,null=True)
    updated_at      = models.DateTimeField(auto_now=True,null=True)



class FinalRecord(TimeStampMixin, models.Model):
    name        = models.CharField(max_length=50, null=True, blank=True)
    age         = models.IntegerField(null=True, blank=True)
    naId        = models.CharField(max_length=14, null=True, blank=True, verbose_name="الرقم القومى")
    hioId       = models.CharField(max_length=14, null=True, blank=True, verbose_name="رقم الحاسب")
    phone       = models.CharField(max_length=11, null=True, blank=True)
    # make many inputs by using comma seperated way lik  a, b, s, v
    illType     = models.CharField(max_length=255, null=True, blank=True, verbose_name = "نوع المرض")
    drugType    = models.CharField(max_length=255, null=True, blank=True, verbose_name = "نوع الأدوية المنصرفة")
    drugAmount  = models.CharField(max_length=255, null=True, blank=True, verbose_name = "كمية الأدوية المنصرفة")
    drugUnit    = models.CharField(max_length=255, null=True, blank=True, verbose_name = "الوحدة الدوائية")

    def __str__(self) -> str:
        return self.name