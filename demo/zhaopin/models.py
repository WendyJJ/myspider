from django.db import models

# Create your models here.
class ZhaoPin(models.Model):
    id = models.IntegerField(primary_key=True,unique=True)
    url = models.CharField(max_length=500)
    pname = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    company = models.CharField(max_length=100)
    ptype = models.CharField(max_length=50)
    welfare = models.CharField(max_length=300)
    smoney = models.IntegerField()
    emoney = models.IntegerField()
    eyear = models.IntegerField()
    age = models.CharField(max_length=50)
    degree = models.CharField(max_length=50)
    time_pub = models.CharField(max_length=100)
    desc_job = models.TextField()
    crawl_time = models.DateField()
    webname = models.CharField(max_length=20)

    class Meta:
        db_table = 'liepin'