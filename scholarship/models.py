from django.db import models

# Create your models here.
class Scholar(models.Model):

    title = models.CharField(max_length=100)
    firstname_eng = models.CharField(max_length=100)
    lastname_eng = models.CharField(max_length=100)

    year_start = models.IntegerField()
    year_end = models.IntegerField()
    programmeName = models.CharField(max_length=200, null=True)
    thesisTitle = models.CharField(max_length=500, null=True)
    scholarshipName = models.CharField(max_length=100, null=True)

    latestJob = models.CharField(max_length=500, null=True)
    sharing = models.CharField(max_length=10000)
    status = models.CharField(max_length=50, default='past')

    pic = models.ImageField(blank=True, null=True, upload_to='scholar/')

    def __str__(self):
        return self.firstname_eng + self.lastname_eng
