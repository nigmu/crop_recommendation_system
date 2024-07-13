from django.db import models

# Create your models here.

class upload_soil_data_class(models.Model):
    id = models.AutoField(primary_key=True)
    N = models.FloatField()
    P = models.FloatField()
    K = models.FloatField()
    Temperature = models.FloatField()
    Humidity = models.FloatField()
    Ph = models.FloatField()
    Rainfall = models.FloatField()
    predicted_crop = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Soil Data {self.id}"
