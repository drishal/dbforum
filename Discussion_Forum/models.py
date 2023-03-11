from django.db import models
from ckeditor.fields import RichTextField

class forum(models.Model):
    name=models.CharField(max_length=200,default="anonymous" )
    email=models.CharField(max_length=200,null=True)
    topic= models.CharField(max_length=300)
    # description = models.TextField(max_length=1000)
    description = RichTextField(blank=True, null=True)
    date_created=models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return str(self.topic)

class Discussion(models.Model):
    forum = models.ForeignKey(forum,on_delete=models.CASCADE)
    # forum_id = models.IntegerField()
    name=models.CharField (max_length=200,default="anonymous")
    # comment = models.TextField(max_length=1000)
    comment = RichTextField(blank=True, null=True)

    def __str__(self):
        return str(self.forum)

