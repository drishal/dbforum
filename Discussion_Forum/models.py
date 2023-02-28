from django.db import models

class forum(models.Model):
    name=models.CharField(max_length=200,default="anonymous" )
    email=models.CharField(max_length=200,null=True)
    topic= models.CharField(max_length=300)
    description = models.TextField(max_length=1000)
    link = models.CharField(max_length=100, blank=True)
    date_created=models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return str(self.topic)

class Discussion(models.Model):
    forum = models.ForeignKey(forum,blank=True,on_delete=models.CASCADE)
    name=models.CharField (max_length=200,default="anonymous")
    discuss = models.TextField(max_length=1000)

    def __str__(self):
        return str(self.forum)
