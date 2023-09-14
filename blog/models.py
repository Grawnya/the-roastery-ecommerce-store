from django.db import models


class Blog(models.Model):
    """Blog model."""

    heading = models.CharField(max_length=200)
    blog_body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Readable string for blog."""
        return f'{self.heading}: {self.blog_body}'


class OurStory(models.Model):
    """Model of ecommerce store's timeline."""

    event_id = models.CharField(max_length=24,
                                null=False,
                                editable=False)
    date_occurred = models.CharField(max_length=50)
    event = models.CharField(max_length=50)

    def __str__(self):
        """Readable string for timeline."""
        return f'{self.event} occurred in {self.date_occurred}'
