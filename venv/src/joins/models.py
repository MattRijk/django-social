from django.db import models

# Create your models here.
class Join(models.Model):
    email = models.EmailField()

    # auto_now_add -> when it was added to the database ==> set the time.
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    # auto_now -> When the model was updated ==> set the time.
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)


    # name = models.CharField(max_length=100, primary_key=True)
    def __unicode__(self):
        return "%s" %(self.email)

    # def name(self):
    #     return self.name