from django.db import models


class TimeStampedModel(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class MedicineName(TimeStampedModel):
    name = models.CharField(max_length=200)


class MedicineForm(TimeStampedModel):
    name = models.CharField(max_length=200)


class MedicineDose(TimeStampedModel):
    unit = models.CharField(max_length=200)
    value = models.CharField(max_length=200, default='')


class ActiveSubstance(TimeStampedModel):
    name = models.CharField(max_length=200, default='')


class PackageContent(TimeStampedModel):
    unit = models.CharField(max_length=200)
    value = models.CharField(max_length=200, default='')
    original_content = models.CharField(max_length=200, default='')


class EAN(TimeStampedModel):
    value = models.IntegerField()


class Refund(TimeStampedModel):
    name = models.CharField(max_length=200)


class Surcharge(TimeStampedModel):
    value = models.FloatField(default=0)


# Nazwa leku, Postać leku, Dawka substancji czynnej w leku, Zawartość opakowania, Nazwa substancji czynnej,
# Kod EAN, Zakres wskazań objętych przez refundację, Wysokość dopłaty świadczeniobiorcy (klienta).
class RowA(TimeStampedModel):
    name = models.ForeignKey(MedicineName, on_delete=models.CASCADE)
    form = models.ForeignKey(MedicineForm, on_delete=models.CASCADE)
    dose = models.ForeignKey(MedicineDose, on_delete=models.CASCADE)
    substance = models.ForeignKey(ActiveSubstance, on_delete=models.CASCADE)
    content = models.ForeignKey(PackageContent, on_delete=models.CASCADE)
    ean = models.ForeignKey(EAN, on_delete=models.CASCADE)
    refund = models.ForeignKey(Refund, on_delete=models.CASCADE)
    surcharge = models.ForeignKey(Surcharge, on_delete=models.CASCADE)
