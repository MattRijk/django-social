from django.db import models

# Create your models here.
class Join(models.Model):
    email = models.EmailField(unique=True)
    ref_id = models.CharField(max_length=120, default='ABC', unique=True)
    ip_address = models.CharField(max_length=120, default='ABC')
    # auto_now_add -> when it was added to the database ==> set the time.
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    # auto_now -> When the model was updated ==> set the time.
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)


    # name = models.CharField(max_length=100, primary_key=True)
    def __unicode__(self):
        return "%s" %(self.email)

    class Meta:
        unique_together = ("email", "ref_id",)

    # def name(self):
    #     return self.name