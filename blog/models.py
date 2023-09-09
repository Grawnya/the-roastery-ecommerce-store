from django.db import models

# Create your models here.
class Blog(models.Model):
    heading = models.CharField(max_length=200)
    blog_body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.heading}: {self.blog_body}'

class OurStory(models.Model):
    event_id = models.CharField(max_length=24, null=False, editable=False)
    date_occurred = models.CharField(max_length=50)
    event = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.event} occurred in {self.date_occurred}'