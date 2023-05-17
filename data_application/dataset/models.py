from django.db import models


# Create your models here.
class Dataset(models.Model):
    data_file = models.FileField(upload_to='datasets')
    name = models.CharField(max_length=255)


class ComputedData(models.Model):
    dataset = models.ForeignKey(Dataset, on_delete=models.CASCADE)
    column_name = models.CharField(max_length=255)
    operation = models.CharField(max_length=3)

class PlottedData(models.Model):
    dataset = models.ForeignKey(Dataset, on_delete=models.CASCADE)
    column_x = models.CharField(max_length=255)
    column_y = models.CharField(max_length=255)
